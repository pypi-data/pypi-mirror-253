 
module three_body

  use helpers
  use cutoff  !, only: is_zero, smooth, adjust
  use potential  !, only: compute
  
  implicit none

contains

  subroutine forces(box,pos,ids,for,epot,virial)
    double precision, intent(in)    :: box(:)
    double precision, intent(in)    :: pos(:,:)
    integer,          intent(in)    :: ids(:)
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
    do i = 1,size(pos,2)
       isp = ids(i)
       do j = i+1,size(pos,2)
          jsp = ids(j)
          do k = i+1,size(pos,2)
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
             call is_zero(isp,jsp,rijsq,zero_ij)
             call is_zero(isp,ksp,riksq,zero_ik)
             call is_zero(jsp,ksp,rjksq,zero_jk)
             if (.not.zero_ij .and. .not.zero_ij .and. .not.zero_jk) then
                cos_theta_ijk = dot_product(rij,rik) / sqrt(dot_product(rij,rij) / dot_product(rik,rik))
                ! TODO: remove hij via interface             
                call compute_three_body(isp,jsp,ksp,rijsq,riksq,cos_theta_ijk,uijk,wijk,hijk) ! wij = -(du/dr)/r
                call smooth_three_body(isp,jsp,ksp,rijsq,uij,wij,hij) ! wij = -(du/dr)/r
                epot = epot + uijk
                virial = virial + wijk * rijsq
                for(:,i) = for(:,i) + wijk * rij
                for(:,j) = for(:,j) - wijk * rij
                for(:,k) = for(:,k) - wijk * rij
             end if
          end do
       end do
    end do
  end subroutine forces
  
end module three_body

module interaction_neighbors

  use helpers
  use cutoff  !, only: is_zero, smooth, adjust
  use potential  !, only: compute
  
  implicit none

contains

  subroutine forces(box,pos,ids,neighbors,number_neighbors,for,epot,virial)
    double precision, intent(in)    :: box(:)
    double precision, intent(in)    :: pos(:,:)
    integer,          intent(in)    :: ids(:)
    integer,          intent(in)    :: neighbors(:,:), number_neighbors(:)
    double precision, intent(inout) :: for(:,:)
    double precision, intent(out)   :: epot, virial
    double precision                :: rij(size(pos,1)), rijsq, uij, wij, hbox(size(pos,1)), hij
    integer                         :: i, j, isp, jsp, jn
    logical                         :: zero_ij
    ! TODO: it should be possible to adjust the cutoff from python, but the compute interface is not parsed correctly
    call adjust(compute)
    !$omp parallel workshare
    for = 0.0d0
    !$omp end parallel workshare
    epot = 0.0d0
    virial = 0.0d0
    hbox = box / 2
    do i = 1,size(pos,2)
       isp = ids(i)
       do jn = 1,number_neighbors(i)
          j = neighbors(jn,i)
          !if (newton) then
          !   if (j<i) cycle
          !end if
          jsp = ids(j)
          call distance(i,j,pos,rij)
          call pbc(rij,box,hbox)
          call dot(rij,rij,rijsq)
          call is_zero(isp,jsp,rijsq,zero_ij)          
          if (.not.zero_ij) then
             ! TODO: remove hij via interface             
             call compute(isp,jsp,rijsq,uij,wij,hij) ! wij = -(du/dr)/r
             call smooth(isp,jsp,rijsq,uij,wij,hij) ! wij = -(du/dr)/r
             epot = epot + uij
             virial = virial + wij * rijsq
             for(:,i) = for(:,i) + wij * rij
             for(:,j) = for(:,j) - wij * rij
          end if
       end do
    end do
  end subroutine forces

end module interaction_neighbors

