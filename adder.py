# warning: nonsense
import pennylane as qml

dev = qml.device('default.qubit', wires=11)

B = 1
X = 5
Y = 6
mod = 7

x_wires = [0,1,2]
y_wires = [3,4,5]
output_wires = [7,8,9]
work_wires = [6,10]

@qml.qnode(dev)
def circuit():
    qml.BasisEmbedding(X, wires=x_wires)
    qml.BasisEmbedding(Y, wires=y_wires)
    qml.BasisEmbedding(B, wires=output_wires)
    
    # here I guess would be the "piecewise" twos complement negation??
    '''qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[0,2])
    qml.Adder(1, x_wires[0], mod, work_wires=work_wires)
    qml.Adder(1, x_wires[1], mod, work_wires=work_wires)
    qml.Adder(1, x_wires[2], mod, work_wires=work_wires)'''
    
    # "combining" the result?
    qml.OutAdder(X, x_wires, output_wires=output_wires, work_wires=work_wires)
    return qml.state()

state = circuit()

print(state)