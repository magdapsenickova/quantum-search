import pennylane as qml

dev = qml.device('default.qubit', wires=3)

X = [1,1,1]
Y = [1,0,1]
x_wires = [0,1,2]
mod = 8
work_wires = [4,5]

@qml.qnode(dev)
def circuit2(feature):
    qml.BasisEmbedding(features=feature, wires=range(3))
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[0,2])
    qml.Adder(X, x_wires, mod, work_wires)
    return qml.state()

state = circuit2(Y)

print(state)