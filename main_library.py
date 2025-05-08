import numpy as np
import itertools

#### options of target state ####
def tensor_T(n):
    """ This function returns the tensor product of n T gates 
    as a (complex) numpy 1d-array """
    return np.array([1.0]*(2**n-1)+[np.exp(1j*np.pi/4)])

def U(theta,n):
    """ This function returns the C^(n-1)-U(theta) on n qubits 
    as a (complex) numpy 1d-array """
    return np.array([1.0]*(2**n-1)+[np.exp(1j*theta)])

def multi_CZ(n):
    """ This function returns the C^(n-1)-Z gate on n qubits 
    as a (float) numpy 1d-array """
    out = np.array([1.0]*(2**n-1)+[-1.0])
    if n<=1:
        out = 0
        print("Warning: multi_CZ({}) is not defined".format(n))
    return out

def multi_CS(n):
    """ This function returns the C^(n-1)-S gate on n qubits 
    as a (complex) numpy 1d-array """
    out = np.array([1.0]*(2**n-1)+[1j])
    if n<=1:
        out = 0
        print("Warning: multi_CS({}) is not defined".format(n))
    return out

##### auxiliary functions for generating decompositions elements #####
def symmetric_Rs(n):
    """ This function returns a list of all symmetric matrices R of size n x n. 
    They are in one-to-one correspondence with the elements of the diagonal Clifford group
    on n qubits in the quocient space Clifford(n)/Paulis(n)."""
    Rs=[]
    bs=list(itertools.product([0,1], repeat=n)) # list of possible bitstrings of length n
    os=list(itertools.product([0,1], repeat=(sum([n-1-i for i in range(n-1)])))) # same for upper off-diagonal number of elements
    for b in bs:
        for o in os:
            R=np.zeros((n,n),dtype=np.int8)
            for i in range(n):
                R[i,i]=b[i] # a 1 here corresponds to a phase gate on qubit i
                for j in range(n-1-i):
                    if o[sum([n-k-1 for k in range(i)])+j]==1:
                        R[i,i+j+1]=1 # a 1 here corresponds to a CZ gate between the indexed qubits
                        R[i+j+1,i]=1
            Rs.append(R.copy())
    return Rs