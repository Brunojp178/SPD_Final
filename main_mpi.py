import numpy as np
from mpi4py import MPI
import itertools

def Main():
    # MPI var's.
    comm = MPI.COMM_WORLD
    nprocs = comm.Get_size()
    rank = comm.Get_rank()

    vect = []

    file_path = "D:\Workspace\Python\SPD\SPD_Final\DATA\GCF_000001735.4_TAIR10.1_genomic.fna"

    # This is for when u copy and paste the path, so u don't have to do manually
    file_path = file_path.replace("\\", "/")

    # Rank 0 open the file and scatter it
    if rank == 0:
        f = open(file_path, 'r')
        
        # Using this to get the index of the last line on the file.
        for last_line_i, line in enumerate(f):
            vect.append(line)

        # Reset file reader buffer.
        f.seek(0,0)

        # Using the last index we calculate the interval size that every process will be reading in the file
        #  and send this var to all process
        n = int(last_line_i/nprocs)
        
        # if the result of the division is not a natural number, we add one to "n" so we don't miss nothing when reading the array
        if (last_line_i%nprocs) != 0:
            n += 1
    else:
        n = None
        vect = []
    
    n = comm.bcast(n, root=0)
    vect = comm.bcast(vect, root=0)

    count_adenina = 0
    count_guanina = 0
    count_citosina = 0
    count_timina = 0

    # Calculo do intervalo onde cada thread vai ler o vetor
    interval_start = int(rank * n)
    interval_end = int((rank + 1) * n)
    
    # Utilizando biblioteca itertools para ler apenas intervalo
    for row in itertools.islice(vect, interval_start, interval_end):
        # Excluindo a linha de metadados
        if row[0] != ">":
            for i in row:
                if i == "a" or i == "A":
                    count_adenina += 1
                elif i == "g" or i == "G":
                    count_guanina += 1
                elif i == "c" or i == "C":
                    count_citosina += 1
                elif i == "t" or i == "T":
                    count_timina += 1

    # Reune todos os contadores em um dicionario e reune o dicionario de cada thread em um dicionario no thread 0
    results_dictionary = { "Adenina":count_adenina, "Guanina":count_guanina, "Citosina":count_citosina, "Timina":count_timina}
    gather_dictionary = comm.gather(results_dictionary, root=0)

    # Como no thread 0 a função gather gerou um array de dicionarios, realizamos a soma dos elementos do dicionario para obtermos uma contagem única
    if rank == 0:
        count_a = 0
        count_g = 0
        count_c = 0
        count_t = 0

        for row in gather_dictionary:
            count_a += row.get("Adenina")
            count_g += row.get("Guanina")
            count_c += row.get("Citosina")
            count_t += row.get("Timina")

        # Redefinimos o results_dictionary anteriormente usado como o resultado final da soma.
        results_dictionary = { "Adenina":count_a, "Guanina":count_g, "Citosina":count_c, "Timina":count_t}
        print("Maior recorrência da base nitrogenada:", max(results_dictionary), results_dictionary.get(max(results_dictionary)))

if __name__ == "__main__":
    Main()