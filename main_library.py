import numpy as np

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
    as a (complex) numpy 1d-array """
    out = np.array([1.0]*(2**n-1)+[-1.0])
    if n<=1:
        out = 0
    return out

def multi_CS(n):
    """ This function returns the C^(n-1)-S gate on n qubits 
    as a (complex) numpy 1d-array """
    out = np.array([1.0]*(2**n-1)+[1j])
    if n<=1:
        out = 0
    return out