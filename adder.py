# trying to add??

import pennylane as qml
import matplotlib.pyplot as plt
import numpy as np

x = 1
k = 3
mod = 7

x_wires =[0,1,2,3]
work_wires=[4,5]

basis_state = [1, 0]

dev = qml.device("default.qubit", wires=2)

dev = qml.device("default.qubit", shots=1)
@qml.qnode(dev)
def circuit():
    qml.BasisEmbedding(x, wires=x_wires)
    qml.Adder(k, x_wires, mod, work_wires)
    return qml.sample(wires=x_wires)

state = circuit()

print(state)





