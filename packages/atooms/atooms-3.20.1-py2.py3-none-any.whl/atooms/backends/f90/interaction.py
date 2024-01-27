import numpy
import f2py_jit

from atooms.system.interaction import InteractionBase
from .helpers import _merge_source, _normalize_path


def _check_polydisperse(species, radius):
    """Check whether system is polydisperse"""
    # Make sure all species are identical
    poly = False
    tolerance = 1e-15
    if numpy.all(species == species[0]):
        delta = abs(radius.min() - radius.max())
        if delta > tolerance * radius.mean():
            poly = True
    return poly

# Aliases for cutoffs and potentials (for backward compatibility)
# First entry of tuple is the alias, second one is the official name
aliases = [('linear_cut_shift', 'cut_shift_linear'),
           ('quadratic_cut_shift', 'cut_shift_quadratic'),
           ('harmonic_potential', 'harmonic'),
           ]

class Interaction(InteractionBase):

    """
    A fortran 90 backend to compute interactions between particles.

    The idea is to stitch together four fortran modules:

    1) a helpers module, which define common subroutines needed to
    compute several types of interaction terms

    2) a potential module, which defines subroutines to initialize and
    compute a potential between particles

    3) a cutoff module, which defines subroutines to initialize, cut
    off and smooth a potential around some distance

    4) an interaction module, which uses the above ones to compute the
    total interaction energy, forces, etc.

    The above modules are merged in a single source at run time and
    compiled using f2py-jit.
    """
    
    def __init__(self, model, neighbor_list=None,
                 interaction='interaction.f90', helpers='helpers.f90',
                 inline=True, inline_safe=False, debug=False,
                 parallel=False, search_dir=None):
        """
        The interaction `model` is a dictionary with "potential" and
        "cutoff" keys. Each key is a dictionary of potential type and
        parameters, with the following layout:

        model = {
          "name": "lennard_jones",
          "potential": [{
              "type": "lennard_jones",
              "parameters": {"epsilon": [[1.0]], "sigma": [[1.0]]}
          }],
          "cutoff": [{
              "type": "cut_shift",
              "parameters": {"rcut": [[2.5]]}
          }]
        }

        The `type` variables must match the names of the fortran
        modules defined by the `f90` backend.

        The dictionaries `parameters` must match the input arguments
        of the `init` subroutines of the selected fortran modules.

        The entries of the `parameters` dictionaries must be (nsp,
        nsp) arrays, where nsp is the number of chemical species
        defined by the model (in the above example, nsp=1).

        The `name` key can contain a string that defines the name of
        the model.
        """
        InteractionBase.__init__(self)
        self.neighbor_list = neighbor_list
        self.order = 'F'
        self.observable.append('gradw')
        self.variables = {'box': 'cell.side:float64',
                          'pos': 'particle.position:float64',
                          'ids': 'particle.species:int32',
                          'rad': 'particle.radius:float64'}
        self.model = model
        # Cache for polydisperse system
        self._polydisperse = None

        # At this stage we expect a model dictionary
        # Normalize paths
        for entry in model["potential"] + model["cutoff"]:
            for alias in aliases:
                if entry["type"] == alias[0]:
                    entry["type"] = alias[1]
                    break
            if "path" not in entry:
                entry["path"] = _normalize_path(entry.get("type"), search_dir)

        # Loop over individual potentials and build interaction modules
        self._uid = []
        for _potential, _cutoff in zip(model['potential'], model['cutoff']):
            potential = _potential.get('path')
            potential_parameters = _potential.get('parameters')
            cutoff = _cutoff.get('path')
            cutoff_parameters = _cutoff.get('parameters')
            potential = _normalize_path(potential, search_dir)
            cutoff = _normalize_path(cutoff, search_dir)

            # Merge all sources into a unique source blob
            source = _merge_source(helpers, potential, cutoff, interaction)

            # Inline subroutines
            if inline:
                from f2py_jit.finline import inline_source
                # TODO: depending on f2py-jit version we can inline compute and smooth as well but this should be checked for bacward compatibility
                if inline_safe:
                    source = inline_source(source, ignore='compute,smooth,adjust,forces')
                elif inline:
                    source = inline_source(source, ignore='adjust,forces')

            # Compile and bundle the module with f2py
            args = ''
            opt_args = '-ffree-form -ffree-line-length-none'
            if debug:
                opt_args += ' -O3 -pg -fbounds-check'
            else:
                opt_args += ' -O3 -ffast-math'
            if parallel:
                opt_args += ' -fopenmp'
                args += ' -lgomp'
            extra_args = '--opt="{}" {}'.format(opt_args, args)

            # Build a unique module for each potential
            # Every model with its own parameter combination corresponds to a unique module
            # and can be safely reused (up to changes in interaction / helpers)
            uid = f2py_jit.build_module(source,
                                        metadata={"interaction": interaction,
                                                  "helpers": helpers,
                                                  "parallel": parallel,
                                                  "potential": [potential, potential_parameters],
                                                  "cutoff": [cutoff, cutoff_parameters]},
                                        extra_args=extra_args)
            # Setup potential and cutoff parameters
            _interaction = f2py_jit.import_module(uid)
            _interaction.potential.init(**potential_parameters)
            _interaction.cutoff.init(**cutoff_parameters)

            # Store module name (better not store the module itself, else we cannot deepcopy)
            self._uid.append(uid)

    def __str__(self):
        txt = 'interaction: f90 backend\n'
        if isinstance(self.model, dict):
            import pprint
            txt += 'model: ' + pprint.pformat(self.model) + '\n'
        else:
            txt += 'model: ' + self.model + '\n'
        if self.neighbor_list:
            txt += 'neighbor list: ' + str(self.neighbor_list)
        return txt

    def compute(self, observable, box, pos, ids, rad):
        """
        Compute `observable` from this interaction
        """
        # Check if system is polydisperse (cached)
        if self._polydisperse is None:
            self._polydisperse = _check_polydisperse(ids, rad)
        if self.neighbor_list is None:
            self._compute(observable, box, pos, ids, rad)
        else:
            self._compute_with_neighbors(observable, box, pos, ids, rad)

    def _initialize(self, observable, pos):
        if observable in ['forces', 'energy', None]:
            if self.forces is None or self.forces.shape != pos.shape:
                self.forces = numpy.zeros_like(pos, order='F')
            # We set these variables as 0-dim array to modify them inplace
            # We cast them as float at the end of compute()
            self.energy, self.virial = numpy.array(0.0), numpy.array(0.0)
        elif observable == 'energies':
            if not hasattr(self, 'energies') or self.energies.size != pos.shape[1]:
                self.energies = numpy.zeros(pos.shape[1])
        elif observable == 'gradw':
            if not hasattr(self, 'gradw') or self.gradw.shape != pos.shape:
                self.gradw = numpy.zeros_like(pos, order='F')
        elif observable == 'hessian' or self.hessian:
            ndim, N = pos.shape
            if self.hessian is None or self.hessian.shape != (ndim, N, ndim, N):
                self.hessian = numpy.ndarray((ndim, N, ndim, N), order='F')

    def _compute(self, observable, box, pos, ids, rad):
        # Initialize variables
        self._initialize(observable, pos)

        # We set the variables to zero for the first interaction
        zero = True
        for uid in self._uid:
            # Load appropriate module according to polydispersity
            _interaction = f2py_jit.import_module(uid)
            if not self._polydisperse:
                f90 = _interaction.interaction
            else:
                f90 = _interaction.interaction_polydisperse

            # Compute the interaction cumulating terms
            if observable in ['forces', 'energy', None]:
                f90.forces(zero, box, pos, ids, rad, self.forces, self.energy, self.virial)
            elif observable == 'energies':
                f90.energies(zero, box, pos, ids, rad, self.energies)
            elif observable == 'gradw':
                assert len(self._uid) == 1, 'cannot compute gradw with multiple potentials'
                f90.gradw(zero, box, pos, ids, rad, self.gradw)
            elif observable == 'hessian':
                f90.hessian(zero, box, pos, ids, rad, self.hessian)

            # If there is more than interaction we cumulate them
            # so we do not zero the variables anymore
            zero = False

        if observable in ['forces', 'energy', None]:
            self.energy, self.virial = float(self.energy), float(self.virial)

    def _compute_with_neighbors(self, observable, box, pos, ids, rad):
        # Initialize variables
        self._initialize(observable, pos)

        # We set the variables to zero for the first interaction
        zero = True
        for uid in self._uid:
            _interaction = f2py_jit.import_module(uid)
            if not self._polydisperse:
                f90 = _interaction.interaction_neighbors
                cutoff = _interaction.cutoff.rcut_
            else:
                f90 = _interaction.interaction_polydisperse_neighbors
                # We set the cutoff to the largest particles: the worst
                # case scenario of
                #
                # rcut(i,j) = rcut * (radius(i) + radius(j))
                #
                # is when radius(i) = radius(j) = max(radius).
                #
                # This is a bit inefficient but keeps the code more
                # general and it works also with linked cells
                largest_radius = numpy.max(rad)
                cutoff = _interaction.cutoff.rcut_ * (largest_radius*2)
            if observable in ['forces', 'energy', None]:
                self.neighbor_list.adjust(box, pos, cutoff)
                self.neighbor_list.compute(box, pos, ids)
                f90.forces(zero, box, pos, ids, rad,
                           self.neighbor_list.neighbors,
                           self.neighbor_list.number_of_neighbors,
                           self.forces, self.energy, self.virial)
            elif observable == 'energies':
                f90.energies(zero, box, pos, ids, rad,
                             self.neighbor_list.neighbors,
                             self.neighbor_list.number_of_neighbors,
                             self.energies)
            elif observable == 'gradw':
                raise ValueError('gradw not implemented with neighbors')
            elif observable == 'hessian':
                f90.hessian(zero, box, pos, ids, rad,
                            self.neighbor_list.neighbors,
                            self.neighbor_list.number_of_neighbors,
                            self.hessian)
            zero = False

        if observable in ['forces', 'energy', None]:
            self.energy, self.virial = float(self.energy), float(self.virial)
