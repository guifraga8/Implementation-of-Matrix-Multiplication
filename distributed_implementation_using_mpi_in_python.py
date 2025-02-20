from mpi4py import MPI
import numpy as np
import time

# Tamanho fixo das matrizes
N = 10000

# Inicializa as matrizes A e B com valores fixos
def inicializar_matrizes():
    A = np.full((N, N), 5)  # Preenche a matriz A com o valor 5
    B = np.full((N, N), 3)  # Preenche a matriz B com o valor 3
    return A, B

# Função para multiplicação de matrizes em paralelo
def multiplicar_matrizes_paralelo(A, B, rank, size):
    C = np.zeros((N, N))
    rows_per_process = N // size  # Divisão das linhas entre os processos
    
    # Cada processo calcula as linhas da matriz resultado
    for i in range(rank * rows_per_process, (rank + 1) * rows_per_process):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]
    return C

# Função para combinar os resultados dos processos
def coletar_resultados(C, rank, size, comm):
    if rank == 0:
        final_C = np.zeros((N, N))
        # Processo 0 coleta os resultados dos outros processos
        final_C[:N//size, :] = C[:N//size, :]
        for i in range(1, size):
            comm.Recv(final_C[i*(N//size):(i+1)*(N//size), :], source=i, tag=11)
        return final_C
    else:
        # Outros processos enviam suas partes da matriz para o processo 0
        comm.Send(C, dest=0, tag=11)

# Função principal
def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    # Apenas o processo 0 inicializa as matrizes
    if rank == 0:
        A, B = inicializar_matrizes()
    else:
        A = B = None
    
    # Distribui as matrizes A e B para todos os processos
    A = comm.bcast(A, root=0)
    B = comm.bcast(B, root=0)
    
    # Mede o tempo de execução da multiplicação
    inicio = time.time()
    
    # Multiplicação paralela
    C = multiplicar_matrizes_paralelo(A, B, rank, size)
    
    # Coleta os resultados no processo 0
    C_final = coletar_resultados(C, rank, size, comm)
    
    # Apenas o processo 0 salva o resultado
    if rank == 0:
        np.savetxt("resultado_mpi.txt", C_final, fmt='%d')
    
    fim = time.time()
    if rank == 0:
        print(f"Tempo de execução paralelo: {fim - inicio} segundos")

if __name__ == "__main__":
    main()
