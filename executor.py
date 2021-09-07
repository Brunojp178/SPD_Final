import sys
import os
import time

def Main():
    # caminho para encontrar os arquivos .py
    self_path = os.getcwd()
    self_path = self_path.replace("\\", "/")

    # numero de execuções
    n_exec = 10

    # Roda a versão sequencial
    program_path = self_path + "/main.py"
    # Roda a versão mpi
    program_path2 = self_path + "/main_mpi.py"

    # tempos de execução
    exec_time = []
    exec_time1 = []
    exec_time2 = []
    exec_time3 = []
    exec_time4 = []

    command = "python " + program_path
    command1 = "mpiexec -n 5 python " + program_path2
    command2 = "mpiexec -n 10 python " + program_path2
    command3 = "mpiexec -n 15 python " + program_path2
    command4 = "mpiexec -n 20 python " + program_path2
    
    # roda cada commando 'n_exec' número de vezes
    for i in range(n_exec):
        exec_time.append(run_program(command))
        exec_time1.append(run_program(command1))
        exec_time2.append(run_program(command2))
        exec_time3.append(run_program(command3))
        exec_time4.append(run_program(command4))
    
    # tempo médio de cada um dos programas
    exec_time = sum(exec_time)/n_exec
    exec_time1 = sum(exec_time1)/n_exec
    exec_time2 = sum(exec_time2)/n_exec
    exec_time3 = sum(exec_time3)/n_exec
    exec_time4 = sum(exec_time4)/n_exec
    # Juntando em um array
    exec_times = [exec_time, exec_time1, exec_time2, exec_time3, exec_time4]
    
    print("Média de tempo de cada execução:")
    for i in range(len(exec_times)):
        print(i * 5, "Threads:", exec_times[i])

    # Speedups
    speedup1 = exec_time/exec_time1
    speedup2 = exec_time/exec_time2
    speedup3 = exec_time/exec_time3
    speedup4 = exec_time/exec_time4
    # Juntando em um array
    speedups = [speedup1, speedup2, speedup3,speedup4]
    
    print("Speedups:")
    for i in range(len(speedups)):
        print((i + 1)*5, "Threads:", speedups[i])

# Method to run the program and get the execution time
def run_program(command):
    starting_time = time.time()
    os.system(command)
    ending_time = time.time() - starting_time
    return ending_time

if __name__ == "__main__":
    Main()