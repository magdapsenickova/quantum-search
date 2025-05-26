# warning: nonsense
import pennylane as qml

dev = qml.device('default.qubit', wires=6)

X = [1,1,1]
Y = [1,0,1]
x_wires = [0,1,2]
work_wires = [4,5]
output_wires = [6,7]
mod = 2

@qml.qnode(dev)
def circuit2(feature):
    qml.BasisEmbedding(features=feature, wires=range(3))
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[0,2])
    qml.Adder(1, x_wires[0], mod, work_wires=work_wires)
    qml.Adder(1, x_wires[1], mod, work_wires=work_wires)
    qml.Adder(1, x_wires[2], mod, work_wires=work_wires)
    qml.OutAdder(X, x_wires, output_wires=output_wires, work_wires=work_wires)
    return qml.state()

state = circuit2(Y)

print(state)