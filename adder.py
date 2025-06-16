import pennylane as qml

bitstrings = ["010", "111", "110", "000"]

dev = qml.device(name="default.qubit",shots=1)

@qml.qnode(dev)
def circuit(feature_vector):

    #qml.BasisEmbedding(2, wires = [0,1])
    qml.Hadamard(wires = [0])
    qml.Hadamard(wires = [1])
    
    qml.QROM(bitstrings = bitstrings,
    control_wires = [0,1],
    target_wires = [2,3,4],
    work_wires = None)

    # negating
    qml.BasisEmbedding(features=feature_vector, wires=range(3))
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[0, 2])
    qml.Adder(1, x_wires=[2])

    # subtracting the data point
    qml.Adder(0, x_wires=[1])
    qml.Adder(1, x_wires=[2])
    
    # converting to sign-magnitude
    qml.Adder(-1, x_wires=[2])
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[0, 2])

    return qml.sample()

X = [1,1,1]
print(circuit(X))