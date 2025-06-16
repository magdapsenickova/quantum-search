import pennylane as qml 
wires = qml.registers({"x": 2, "output": 4})

def f(x):
    return x ** 2

@qml.qnode(qml.device("default.qubit", shots = 1))
def circuit():
    # load values of x
    qml.BasisEmbedding(3, wires=wires["x"])

    # apply the polynomial
    qml.OutPoly(
        f,
        input_registers = [wires["x"]],
        output_wires = wires["output"])

    return qml.sample(wires=wires["output"])

print(circuit())