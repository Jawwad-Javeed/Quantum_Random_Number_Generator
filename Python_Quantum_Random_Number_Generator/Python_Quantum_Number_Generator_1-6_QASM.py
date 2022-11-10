#Import Qiskit and Qiskit.Visualization
import qiskit
from qiskit import QuantumCircuit, assemble, Aer,execute
from qiskit.visualization import plot_histogram,plot_bloch_multivector
#Set Current Qiskit Backend to QASM Simulator 
#Switch if using IBM Quantum Computers
sim=Aer.get_backend('qasm_simulator')

#Intializes 3 Qubits and 3 Classical Bits
qc=QuantumCircuit(3,3)

#Amounts of times Simulation is run
sim_run=1

#Sets every Qubit in superposition(|+> basis) using Hadamard Gate
#50% chance of |0> and 50% chance of |1>
for i in range(0,3):
    qc.h(i)
    
#Creates barrier between gates and measurements for qc.draw() and optimization level
qc.barrier()


#Collapses superposition of every Qubit and assigns value to corrosponding Classical bit
for x in range(0,3):
    qc.measure(x,x)
    
#Draws Quantum Circuit
#qc.draw()
    
#Function to convert Qubit Binary to Base 10 and displays randomly generated number
def QASM_Generate():
    #memory=True to access indivual simulation qubit measurement values
    job=execute(qc,sim,shots=sim_run,memory=True)
    result=job.result()
    counts=result.get_counts()
    memory=result.get_memory()
    #Converts Qubit Binary to Base 10
    int_value=int(memory[0],2)
    
    #Check int_value throughout iterations
    #print(int_value)
    
    if int_value==7 or int_value==0:
        QASM_Generate()
    else:
        return int_value
        

#QASM_Generate()