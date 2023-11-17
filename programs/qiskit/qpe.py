from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT
import numpy as np

n_qubits = 3
U = QuantumCircuit(1)

U.x(0)

qpe = QuantumCircuit(n_qubits + 1, n_qubits)
qpe.h(range(n_qubits))

for qubit in range(n_qubits):
    repetitions = 2**qubit
    for _ in range(repetitions):
        qpe.append(U.control(), [qubit, n_qubits])

qpe.append(QFT(n_qubits, do_swaps=False).inverse(), range(n_qubits))

qpe.measure(range(n_qubits), range(n_qubits))

print(qpe.draw())

simulator = Aer.get_backend('qasm_simulator')
result = execute(qpe, simulator, shots=1024).result()
counts = result.get_counts(qpe)
print(counts)
