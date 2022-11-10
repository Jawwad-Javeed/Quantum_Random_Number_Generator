#Import Qiskit
import qiskit
from qiskit import QuantumCircuit, assemble, Aer,execute

#Set Current Qiskit Backend to QASM Simulator 
#Switch if using IBM Quantum Computers
sim=Aer.get_backend('qasm_simulator')

#Intializes 1 Qubit and 1 Classical Bit
qc=QuantumCircuit(1,1)

#Amounts of times Simulation is run
sim_run=6

#Initial Value of Binomial Distribution count
Start_value=0

#Sets every Qubit in superposition(|+> basis) using Hadamard Gate
#50% chance of |0> and 50% chance of |1>
for i in range(0,1):
    qc.h(i)
    
#Creates barrier between gates and measurements for qc.draw() and optimization level
qc.barrier()


#Collapses superposition of every Qubit and assigns value to corrosponding Classical bit
for x in range(0,1):
    qc.measure(x,x)
    
#Draws Quantum Circuit
#qc.draw()
    
#Function to convert Qubit Binary to Base 10 and displays randomly generated number
def Binomial_Distribution_Counter_Generate():
    #memory=True to access indivual simulation qubit measurement values
    job=execute(qc,sim,shots=sim_run,memory=True)
    result=job.result()
    counts=result.get_counts()
    memory=result.get_memory()

    for x in range(0,sim_run):
        global Start_Value
        int_value=int(memory[x],2)
        #Adds 1 to Start_Value if |1> else adds 0
        Start_Value=Start_Value+int_value
        
    return Start_Value

#Binomial_Distribution_Counter_Generate()