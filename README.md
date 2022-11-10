# Quantum Random Number Generator

### Developed by:

 - Muhammad Jawwad Javeed Iqbal [[Linkedin](https://linkedin.com/in/jawwad-javeed/)]


## 📚 Table of Contents

* [Project Purpose](#-project-purpose)
* [About](#-about)
* [Required Environment Installations](#%EF%B8%8F-required-environment-installations)
* [File Navigation](#-file-navigation)
  * [Juypter Notebook Files](#juypter-notebook-files)
  * [Python Files](#python-files)
* [Notes](#-notes)
  * [Juypter Notebook](#juypter-notebook)
  * [Python](#python) 

## 📒 Project Purpose

Presently, many modern-day Random Number Generation (RNG) programs do not generate truly randomized numbers, rather they generate pseudorandom numbers determined through specified algorithms.
  
At the same time, current True Random Number Generation (TRNG) programs utilize techniques such as measuring the fluctuations of voltage in order to generate truly random numbers, but are not easily accessible for coding projects.
  
This project aims to resolve both of those issues by using the properties of [Quantum Superposition](https://www.ibm.com/topics/quantum-computing)  alongside IBM's quantum computers in order to generate truly random numbers that can be easily integrated with other coding projects.

## 📖 About
Random Number Generation (RNG) program that uses Quantum Superposition in order to achieve True Random Number Generation that can be integrated with other coding projects.

For this project it is recommended to use one of IBM's Quantum computers instead of a simulator in order to generate truly random numbers, however for testing purposes the [QASM Simulator](https://qiskit.org/documentation/stubs/qiskit.providers.aer.QasmSimulator.html#qasmsimulator) is the most accurate and similar to a real-life Quantum Simulator and is used as a proof of concept.


## 🖥️ Required Environment Installations

```
$ pip install Qiskit

``` 

## 📑 File Navigation
- ### Juypter Notebook Files

  - [`Juypter_Notebook_Quantum_Number_Generator_1-4_Aer.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Juypter_Notebooks_Quantum_Random_Number_Generator/Juypter_Notebook_Quantum_Number_Generator_1-4_Aer.ipynb) uses IBM's [Aer Simulator](https://qiskit.org/documentation/tutorials/simulators/1_aer_provider.html#The-Aer-Simulator) backend in order to emulate Qubit Superposition and provide a histogram of all possible measurement values.
  
  - [`Juypter_Notebook_Quantum_Number_Generator_1-6_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Juypter_Notebooks_Quantum_Random_Number_Generator/Juypter_Notebook_Quantum_Number_Generator_1-6_QASM.ipynb) uses the QASM simulator in order to emulate Qubit Superposition and store the values as a list; the function `Generate()` is then utilized to output a completely randomized number from 1-6.
 
  - [`Juypter_Notebook_Quantum_Number_Generator_1-6_Multi_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Juypter_Notebooks_Quantum_Random_Number_Generator/Juypter_Notebook_Quantum_Number_Generator_1-6_Multi_QASM.ipynb) uses the QASM simulator alongside multiple Qubits and Gates in order to reduce any potential quantum noise effects on the qubit measurements; the function `Generate()` is then utilized to output a completely randomized number from 1-6.
 
    - This program results in the qubits being in either |+> or |-> basis, unlike [`Juypter_Notebook_Quantum_Number_Generator_1-6_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Juypter_Notebooks_Quantum_Random_Number_Generator/Juypter_Notebook_Quantum_Number_Generator_1-6_QASM.ipynb),which has qubits in the |+> state before measurement.
  
  - [`Juypter_Notebook_Quantum_Number_Generator_Binomial_Distribution_Counter_1-6_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Juypter_Notebooks_Quantum_Random_Number_Generator/Juypter_Notebook_Quantum_Number_Generator_Binomial_Distribution_Counter_1-6_QASM.ipynb) uses the QASM simulator in order to emulate iterative binomial distributions.; the function `Generate()` can be utilized to output an iterative binomially distributed number from 1-6.

- ### Python Files 
  - [`Python_Quantum_Number_Generator_1-6_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Python_Quantum_Random_Number_Generator/Python_Quantum_Number_Generator_1-6_QASM.py) uses the QASM simulator in order to emulate Qubit Superposition and store the values as a list; the function `QASM_Generate()` can be utilized to generate a completely randomized number from 1-6.
  
 
  - [`Python_Quantum_Number_Generator_1-6_Multi_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Python_Quantum_Random_Number_Generator/Python_Quantum_Number_Generator_1-6_Multi_QASM.py) uses the QASM simulator alongside multiple qubits and gates in order to reduce any potential quantum noise effects on the qubit measurements; the function `Multi_QASM_Generate()` can be utilized to generate a completely randomized number from 1-6.
      - This program results in the qubits being in either |+> or |-> basis, unlike [`Juypter_Notebook_Quantum_Number_Generator_1-6_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Juypter_Notebooks_Quantum_Random_Number_Generator/Juypter_Notebook_Quantum_Number_Generator_1-6_QASM.ipynb),which has qubits in the |+> state before measurement.
 
  - [`Python_Quantum_Number_Generator_Binomial_Distribution_Counter_1-6_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Python_Quantum_Random_Number_Generator/Python_Quantum_Number_Generator_Binomial_Distribution_Counter_1-6_QASM.py)uses the QASM simulator in order to emulate iterative binomial distributions; the function `Binomial_QASM_Counter_Generate()` can be utilized to generate an iterative binomially distributed number.


## 📝 Notes
- ### Juypter Notebook

  - Activate following code in Juypter notebook files in order to graph Qubit Bloch spheres:

```
qc.save_statevector()
qobj=assemble(qc)
result=sim.run(qobj).result().get_statevector()
plot_bloch_multivector(result)
``` 

- ### Python 
  - Import either `QASM_Generator()` , `Multi_QASM_Generator()`, or `Binomial_Distribution_Counter_Generate()` from [`Python_Quantum_Number_Generator_1-6_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Python_Quantum_Random_Number_Generator/Python_Quantum_Number_Generator_1-6_QASM.py), [`Python_Quantum_Number_Generator_1-6_Multi_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Python_Quantum_Random_Number_Generator/Python_Quantum_Number_Generator_1-6_Multi_QASM.py) or [`Python_Quantum_Number_Generator_Binomial_Distribution_Counter_1-6_QASM.ipynb`](https://github.com/Jawwad-Javeed/Quantum_Random_Number_Generator/blob/main/Python_Quantum_Random_Number_Generator/Python_Quantum_Number_Generator_Binomial_Distribution_Counter_1-6_QASM.py) respectively.


