module interaction

  use helpers
  use cutoff  !, only: is_zero, smooth, adjust
  use potential  !, only: compute
  
  implicit none

contains

  subroutine forces(box,pos,ids,bonds,for,epot,virial)
    double precision, intent(in)    :: box(:)
    double precision, intent(in)    :: pos(:,:)
    integer,          intent(in)    :: ids(:)
    integer,          intent(in)    :: bonds(:,:)
    double precision, intent(inout) :: for(:,:)
    double precision, intent(out)   :: epot, virial
    double precision                :: rij(size(pos,1)), rijsq, uij, wij, hbox(size(pos,1)), hij
    integer                         :: b, i, j, isp, jsp
    !$omp parallel workshare
    for = 0.0d0
    !$omp end parallel workshare
    epot = 0.0d0
    virial = 0.0d0
    hbox = box / 2
    !$omp parallel default(firstprivate) shared(pos,ids,box,hbox,epot,virial,for)
    !$omp do schedule(runtime) reduction(+:epot,virial,for)
    do b = 1,size(bonds,2)
       i = bonds(1,b)
       j = bonds(2,b)
       isp = ids(i)
       jsp = ids(j)
       call distance(i,j,pos,rij)
       call pbc(rij,box,hbox)
       call dot(rij,rij,rijsq)
       call compute(isp,jsp,rijsq,uij,wij,hij) ! wij = -(du/dr)/r
       epot = epot + uij
       virial = virial + wij * rijsq
       for(:,i) = for(:,i) + wij * rij
       for(:,j) = for(:,j) - wij * rij
    end do
    !$omp end parallel
  end subroutine forces
  
end module interaction

