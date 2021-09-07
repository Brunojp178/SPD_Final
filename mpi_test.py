from mpi4py import MPI
import numpy as np

def Main():
    # MPI var's.
    comm = MPI.COMM_WORLD
    nprocs = comm.Get_size()
    rank = comm.Get_rank()

    vect = None
    vect_part = None
    n = None

    file_path = "D:/Workspace/Python/SPD/SPD_Final/teste.txt"

    # This is for when u copy and paste the path, so u don't have to do manually
    file_path = file_path.replace("\\", "/")
    
    if rank == 0:
        vect = []
        for i in range(1, 11):
            vect.append(i)
        n = int(len(vect)/nprocs)

    n = comm.bcast(n, root=0)
    vect_part = np.empty(n, dtype='uint8')
    print("N", n, "\nvect_part.size", len(vect_part))
    # this fucker is not working :D
    comm.Scatter(vect, vect_part, root=0)



    
    
    

    

if __name__ == "__main__":
    Main()