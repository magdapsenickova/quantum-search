import pennylane as qml

n_wires = 3
wires = list(range(n_wires))

def oracle():
    qml.Hadamard(wires[-1])
    qml.Toffoli(wires=wires)
    qml.Hadamard(wires[-1])

dev = qml.device('default.qubit', wires=wires)

@qml.qnode(dev)
def GroverSearch(num_iterations=1):
    for wire in wires:
        qml.Hadamard(wire)

    for _ in range(num_iterations):
        oracle()
        qml.templates.GroverOperator(wires=wires)
    return qml.probs(wires)

print(GroverSearch(num_iterations=1))