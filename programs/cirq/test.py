import cirq
import cirq_google as cg

# Define a qubit at an arbitrary grid location.
qubit = cirq.GridQubit(0, 0)

# Create a circuit (qubits start in the |0> state).
circuit = cirq.Circuit(
    cirq.X(qubit),                     # NOT gate.
    cirq.measure(qubit, key='result')  # Measurement.
)

print(circuit)
