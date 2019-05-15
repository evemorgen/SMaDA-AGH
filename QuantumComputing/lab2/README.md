

## Lab 2

###  Grover’s algorithm

This time, we're gonna try to implement simple algorithm using quantum gates learned in the lab 1.  
If you get stuck at some point or you're just lazy, there is [Jupiters Notebook](quantum3.ipynb) prepared for you.

> **_NOTE:_**  This lab is based on [this medium article by Jonathan Hui](https://medium.com/@jonathan_hui/qc-grovers-algorithm-cd81e61cf248), I highly recommend to read that before jumping into implementation

-----

At first we should get some intuition about Grover’s algorithm, it is a algorith that finds with *high probability* (not for sure!) the unique input to a black box function that produces a particular output value. Other way to describe it - it is an algorithm for finding a needle in a haystack.

For example ([working example here](slides1.ipynb)), we might have the following "haystack" of words:
```python
haystack = ["Hoary Hedgehog", "Gutsy Gibbon", "Oneiric Ocelot", "Precise Pangolin"]
# needle is md5 from one of the words in a haystack
needle = "fd06f6aff94b8f2bade7efde2b949672"
```

If we wanted to find, which word hides under the "needle" `md5`, we would have to iterate over all possible values and check whether md5 of that value is equal to "needle", like this:  

```python
# That is O(n), n = len(haystack)
for word in haystack:
    hashed = md5(word.encode()).hexdigest()
    if hashed == needle:
        print("Aha! Our word is ~~> %s <~~" % word)   
```  

Grover’s algorithm does the same but on "binary" numbers
```python
haystack = [0, 0, 1, 0]
needle = 1

for i, value in enumerate(haystack):
    if value == needle:
        print("Aha! Our 1 is on position %s" % i)
```

----

Alright, let's try to do the same thing in quantum world.  
Try to follow tips in the template, there is a [projectq example](https://github.com/ProjectQ-Framework/ProjectQ/blob/develop/examples/grover.py) and [Jupiters Notebook](quantum3.ipynb) there to help you.  

Here is [projectq docs](https://projectq.readthedocs.io/en/latest/tutorials.html#basic-quantum-program) with quickstart guide  

You might want to use this template
```python
from projectq import MainEngine

# H = Hadamard gate, H|0> -> (|0> + |1>)/sqrt(2)
#                    H|1> -> (|0> - |1>)/sqrt(2)
# X = Pauli X (not) gate.  X|0> -> |1>
#                          X|1> -> |0>
# Z = Pauli Z gate  Z|0> -> |0>
#                   Z|1> -> -|1>
# Measure - perform measurment on a given qubit
# All - performs operation on all qubits in given register
from projectq.ops import H, Z, X, Measure, All

# Loop - in quantum computing there is no such thing as classical loop. It just duplicates given operation n times
# Control - acts like an if statement, code inside is executed based on qubit value passed as argument
from projectq.meta import Loop, Compute, Uncompute, Control

# 1. Initialize things
# create quantum register with 4 qubits, all in state |0>
# allocate one qubit for output function 


# 2. apply hadamard gate to all qubits in the register (uniform superposition)


# 3. apply X pauli gate, then H (Hadamard gate) on the function output qubit - this way we 
# prepare the function output qubit (the one that is flipped to indicate the
# solution. start in state 1/sqrt(2) * (|0> - |1>) s.t. a bit-flip turns
# into a (-1)-phase.

# 4. Here is a "magic function" that states which of our qubits is the "1",
def magic_function(qubits, output):
    # flip 0,1,3 qubits, so 0000 -> 1101, but 0010 -> 1111
    with Compute(engine):
        X | qubits[0]
        X | qubits[1]
        X | qubits[3]
    # if all qubits in register are 1
    with Control(engine, qubits):
        # X(|0> - |1>)/sqrt(2) -> (|1> - |0>)/sqrt(2)
        X | output
    Uncompute(engine)


# 5. Apply magic_function with register and function output qubit (it has to be done in place, sorry FP guys)


# 6. Apply H gate, then X gate to the whole register *inside Compute block*, we will need to uncompute that later


# 7. Flip the last qubit in the register with Z gate if all other qubits of that register are 1 (Control block)


# 8. Uncompute last operation


# 9. Measure whole register value and flush the engine


# 10. Print obtained values


```
