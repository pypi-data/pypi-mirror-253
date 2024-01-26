 
module two_body

  use helpers
  use cutoff  !, only: is_zero, smooth, adjust
  use potential  !, only: compute
  
  implicit none

contains

  subroutine forces(box,pos,ids,terms,for,epot,virial)
    double precision, intent(in)    :: box(:)
    double precision, intent(in)    :: pos(:,:)
    integer,          intent(in)    :: ids(:)
    integer,          intent(in)    :: terms(:,:)
    double precision, intent(inout) :: for(:,:)
    double precision, intent(out)   :: epot, virial
    double precision                :: rij(size(pos,1)), rijsq, uij, wij, hbox(size(pos,1)), hij
    integer                         :: i, j, isp, jsp
    logical                         :: zero_ij
    ! TODO: it should be possible to adjust the cutoff from python, but the compute interface is not parsed correctly
    call adjust(compute)
    for = 0.0d0
    epot = 0.0d0
    virial = 0.0d0
    hbox = box / 2
    do ii = 1,size(terms,2)
       i = terms(1,ii)
       j = terms(2,ii)
       isp = ids(i)
       jsp = ids(j)
       call distance(i,j,pos,rij)
       call pbc(rij,box,hbox)
       call dot(rij,rij,rijsq)
       call compute_stretch(isp,jsp,ksp,rijsq,uij,wij,hij) ! wij = -(du/dr)/r
       epot = epot + uij
       virial = virial + wij * rijsq
       for(:,i) = for(:,i) + wij * rij
       for(:,j) = for(:,j) - wij * rij
    end do
  end subroutine forces
  
end module two_body

