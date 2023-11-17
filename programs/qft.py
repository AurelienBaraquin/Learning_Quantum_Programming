from qiskit import QuantumCircuit, execute, Aer
import numpy as np

nb_qubits = 3

def qft(circuit, n):
    """QFT on the first n qubits in circuit"""
    for i in range(n):
        circuit.h(i)
        for j in range(i+1, n):
            circuit.cp(np.pi/2**(j-i), j, i)
    return circuit

circuit = QuantumCircuit(nb_qubits)

qft(circuit, nb_qubits)

print(circuit.draw())

simulator = Aer.get_backend('qasm_simulator')
circuit.measure_all()
result = execute(circuit, simulator, shots=1024).result()
counts = result.get_counts(circuit)
print(counts)

# Explanation of the program:
# The QFT is a quantum analogue of the discrete Fourier transform (DFT).
# It's often used in quantum algorithms because it provides a way to
# know all possible states of a quantum system at once.
# For example, if we have a 3-qubit system, we can know all possible :
# 000, 001, 010, 011, 100, 101, 110, 111
# It's very similar to the classical Fourier transform, but it's very fast.
