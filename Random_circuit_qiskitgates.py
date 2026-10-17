import qiskit,qiskit.visualization,qiskit_aer,random
from qiskit import transpile,QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def random_circuit (seed,num_gate):
    random.seed(seed)

    qc=QuantumCircuit(2,2)

    for i in range(num_gate):
        r=random.random()

        if r<1/3:
            qubit=random.randint(0,1)
            qc.h(qubit)
        elif r<2/3:
            qubit=random.randint(0,1)
            qc.x(qubit)
        else:
            qc.cx(0,1)
        
    qc.measure([0,1],[0,1])
    sim=AerSimulator()
    compiled=transpile(qc,sim)
    result=sim.run(compiled,shots=1024).result()
    counts=result.get_counts()
    print("counts:",counts)
    print(qc.draw())
    plot_histogram(counts)
    plt.show()


random_circuit(seed=123,num_gate=10)