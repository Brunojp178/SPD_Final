import numpy as np

def Main():
    
    file_path = "D:\Workspace\Python\SPD\SPD_Final\DATA\GCF_000001735.4_TAIR10.1_genomic.fna"

    # This is for when u copy and paste the path, so u don't have to do manually
    file_path = file_path.replace("\\", "/")

    f = open(file_path, 'r')
    
    # Counters
    count_adenina = 0
    count_guanina = 0
    count_citosina = 0
    count_timina = 0

    for line in f:
        # Removing the metadata line and counting every nitrogenous bases
        if line[0] != ">":
            for i in line:
                if i == "a" or i == "A":
                    count_adenina += 1
                elif i == "g" or i == "G":
                    count_guanina += 1
                elif i == "c" or i == "C":
                    count_citosina += 1
                elif i == "t" or i == "T":
                    count_timina += 1

    # Using dictionary to print
    results_dictionary = { "Adenina":count_adenina, "Guanina":count_guanina, "Citosina":count_citosina, "Timina":count_timina}
    print("Maior recorrência da base nitrogenada:", max(results_dictionary), results_dictionary.get(max(results_dictionary)))

    

if __name__ == "__main__":
    # A system call de print do resultado é contabilizada no tempo total.
    Main()