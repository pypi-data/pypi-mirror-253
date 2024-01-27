
module three_body

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
       k = terms(3,ii)
       isp = ids(i)
       jsp = ids(j)
       ksp = ids(k)
       call distance(i,j,pos,rij)
       call distance(i,k,pos,rik)
       call distance(j,k,pos,rjk)
       call pbc(rij,box,hbox)
       call pbc(rik,box,hbox)
       call pbc(rjk,box,hbox)
       call dot(rij,rij,rijsq)
       call dot(rik,rik,riksq)
       call dot(rjk,rjk,rjksq)
       cos_theta_ijk = dot_product(rij,rik) / sqrt(dot_product(rij,rij) / dot_product(rik,rik))
       call compute_bend(isp,jsp,ksp,rijsq,riksq,cos_theta_ijk,uijk,wijk,hijk) ! wij = -(du/dr)/r
       epot = epot + uijk
       virial = virial + wijk * rijsq
       for(:,i) = for(:,i) + wijk * rij
       for(:,j) = for(:,j) - wijk * rij
       for(:,k) = for(:,k) - wijk * rij
    end do
  end subroutine forces
  
end module three_body
