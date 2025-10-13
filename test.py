from sse_library import gen_symmetric_Rs, diagonal_Clifford_from_R, diagonal_paulis, sext_diagonals, tensor_T
import numpy as np

diag=np.vstack(diagonal_paulis(1)).T
Rs=gen_symmetric_Rs(1)
A=np.zeros((2**1,2*len(Rs)*len(diag)), dtype=int)
for i in range(len(Rs)):
    aux=diagonal_Clifford_from_R(Rs[i])*diag
    A[:,i*len(diag):(i+1)*len(diag)]=np.real(aux)
    A[:,len(Rs)*len(diag)+i*len(diag):len(Rs)*len(diag)+(i+1)*len(diag)]=np.imag(aux)
print(sext_diagonals(A,target=tensor_T(1))[0])