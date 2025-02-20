import time
import numpy as np

# Tamanho fixo das matrizes
N = 10000

# Inicializa as matrizes A e B com valores fixos
def inicializar_matrizes():
    A = np.full((N, N), 5)  # Preenche a matriz A com o valor 5
    B = np.full((N, N), 3)  # Preenche a matriz B com o valor 3
    return A, B

# Função para multiplicação das matrizes
def multiplicar_matrizes(A, B):
    C = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]
    return C

# Função para salvar o resultado em um arquivo de texto
def salvar_resultado(C):
    np.savetxt("resultado.txt", C, fmt='%d')

# Função principal
def main():
    # Inicializa as matrizes
    A, B = inicializar_matrizes()
    
    # Mede o tempo de execução da multiplicação
    inicio = time.time()
    
    # Multiplica as matrizes
    C = multiplicar_matrizes(A, B)
    
    # Salva o resultado no arquivo
    salvar_resultado(C)
    
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio} segundos")

if __name__ == "__main__":
    main()
