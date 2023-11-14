from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
sim = AerSimulator()  # make new simulator object
# Create quantum circuit with 2 qubits and 2 classical bits
test_qc = QuantumCircuit(4, 2)

# First, our circuit should encode an input (here '11')
test_qc.x(0)
test_qc.x(1)

# q1 and q2 are the two qubits we want to add
# qout1 and qout2 are the two qubits we want to store the result
def adder(qc, q1, q2, qout1, qout2):
    qc.cx(q1, qout1)
    qc.cx(q2, qout1)
    qc.ccx(q1, q2, qout2)

# Next, it should carry out the adder circuit we created
adder(test_qc, 0, 1, 2, 3)

# Finally, we will measure the bottom two qubits to extract the output
test_qc.measure(2,0)
test_qc.measure(3,1)
print(test_qc.draw())

# Run our circuit on the simulator
job = sim.run(test_qc)
result = job.result()
print(result.get_counts())
