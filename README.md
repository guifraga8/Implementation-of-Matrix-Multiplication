# Matrix Multiplication Implementation: Sequential and Distributed Algorithms

This repository contains the implementation of two matrix multiplication algorithms for fixed-size square matrices (10,000 x 10,000). The first version is sequential, while the second version is parallelized using the MPI (Message Passing Interface) library. Both algorithms initialize the matrices with fixed data and store the result in a text file.

## Requirements

### For the Sequential Version:
- Python 3.x
- Libraries:
  - `numpy` (for matrix manipulation)
  - `time` (to measure execution time)

### For the Distributed Version (MPI):
- Python 3.x
- Libraries:
  - `mpi4py` (for MPI process communication)
  - `numpy` (for matrix manipulation)
  - `time` (to measure execution time)
- MPI-supported environment (e.g., installed with `mpich` or `openmpi`)

## Installation

### Installing Dependencies

1. **Install `numpy`** required for both the sequential and distributed versions:
    ```bash
    pip install numpy
    ```

2. **Install MPI (if not already installed)**, required for the distributed version:
    - On **Ubuntu**:
      ```bash
      sudo apt-get install mpich
      ```
    - On **macOS** (using Homebrew):
      ```bash
      brew install mpich
      ```

3. **Install `mpi4py`** for the distributed version:
    ```bash
    pip install mpi4py
    ```

## How to Run

### 1. **Sequential Version**

The sequential algorithm performs the multiplication of two 10,000 x 10,000 matrices and writes the result to a text file named `resultado.txt`. 

#### Execution Steps:
1. Ensure that the dependencies are installed (numpy is the only required library for this version).
2. Run the Python script:

    ```bash
    python sequential_implementation_in_python.py
    ```

3. The execution time will be printed in the terminal, and the result will be saved in the `resultado.txt` file in the current directory.

#### Output File:
- `resultado.txt`: the resulting matrix from the multiplication will be saved in this file.

---

### 2. **Distributed Version (MPI)**

The distributed version uses the MPI library to parallelize the matrix multiplication by distributing the workload across multiple processes.

#### Execution Steps:

1. **Prepare the Environment:**:
    - Install the dependencies, including `mpi4py` and `numpy`.
    - Ensure that the MPI environment is installed and properly configured.

2. **Run the script using MPI**:
    - The Python script should be executed using the `mpiexec`, which manages the parallel execution of processes.
    - The number of processes can be adjusted based on the system’s capacity and the number of available cores.

    ```bash
    mpiexec -n <number_of_processes> python distributed_implementation_using_mpi_in_python.py
    ```

    Replace `<number_of_processes>` with the desired number of processes. For example, to run with 4 processes:

    ```bash
    mpiexec -n 4 python distributed_implementation_using_mpi_in_python.py
    ```

3. The execution time will be printed in the terminal, and the result will be saved in the `resultado_mpi.txt` file in the current directory.

#### Output File:
- `resultado_mpi.txt`: the resulting matrix from the distributed multiplication will be saved in this file.

---

## Algorithm Explanation

### 1. **Sequential Algorithm**

The sequential algorithm performs the multiplication of two 10,000 x 10,000 matrices \( A \) and \( B \) using the traditional method with three nested loops. Each element’s multiplication is executed directly without optimizations. The result is stored in the `resultado.txt` file.

### 2. **Distributed Algorithm with MPI**

In the distributed version, we use the MPI library to split the workload among multiple processes. Each process computes a portion of the resulting matrix by dividing the number of rows among the processes. Process 0 is responsible for collecting the partial results and assembling the final matrix, which is then saved in the `resultado_mpi.txt` file.

#### Key Steps in the Distributed Code:
- **Matrix Initialization and Distribution**: process 0 initializes the matrices and distributes them to other processes using MPI’s `bcast` function.
- **Parallel Multiplication**: each process computes a portion of the resulting matrix (by dividing the rows) using the same sequential algorithm.
- **Result Collection**: process 0 gathers the computed portions from other processes and constructs the final matrix.

---

## Performance

- **Sequential Version**: the sequential multiplication can be slow for large matrices, especially for 10,000 x 10,000 matrices, due to the time required to compute each element.
  
- **Distributed Version (MPI)**: the distributed version leverages multiple processes to perform the multiplication in parallel. Increasing the number of processes should reduce execution time, but there may be a saturation point where adding more processes no longer provides significant performance gains.

---

## Testing and Validation

Both versions ensure that the input matrices remain the same in every execution, allowing for result comparisons across different runs. After each execution, the output file (`resultado.txt` or `resultado_mpi.txt`) can be checked to verify that the calculations were performed correctly.

---

## Conclusion

This project implements matrix multiplication both sequentially and in a parallelized manner using MPI, aiming to explore performance differences for large matrices. The sequential version serves as a simple starting point, while the distributed version can be scaled to take advantage of multiple cores and machines.

---
