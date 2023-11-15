from qiskit import QuantumCircuit, execute, Aer

circuit = QuantumCircuit(2, 2)

circuit.h(0)

circuit.cx(0, 1)

circuit.measure([0,1], [0,1])

print(circuit.draw())

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, simulator, shots=1000).result()

counts = result.get_counts(circuit)
print(counts)

# Explanation of the results:
# we obtain either 00 or 11, each with more or less equal probability.
# It's because the Hadamard [H] gate puts the first qubit in a superposition state,
# and the CNOT gate entangles the two qubits like a xor gate.
# That mean if q0 is 0, q1 is 0, if q0 is 1, q1 is 1.
# Because 0 XOR 0 = 0, 1 XOR 1 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1.
# And q1 = 0 so if q0 = 0 -> q0 xor q1 = 0 xor 0 = 0. and q0 = q1 = 1 {11, ...}
#               if q0 = 1 -> q0 xor q1 = 1 xor 0 = 1. and q0 = q1 = 0 {00, ...}
