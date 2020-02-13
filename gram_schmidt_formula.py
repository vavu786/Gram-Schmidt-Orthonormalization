# ____________________________________________
# Gram Schmidt Orthonormalization Calculator
# The rows are the new basis vectors
# Enjoy!
# ____________________________________________

import numpy as np
import math as m
from fractions import Fraction

# Defines specific inner product
def inner(v1, v2):
    return np.dot(v1, v2)

# Defines concept of "proj"
def proj(v1, v2):
    return (inner(v1, v2)/inner(v2, v2))*v2
    
# Orthogonalizes the vectors    
def orthog(vecnum, ibasis, fbasis):
    # vecnum is the nth vector in the basis vectors
    if vecnum == 0:
        fbasis[0,:] = ibasis[0,:]
    if vecnum != 0:
        fbasis[vecnum,:] = ibasis[vecnum,:] - sum(proj(ibasis[vecnum,:], fbasis[x,:]) for x in range(vecnum))
    
# Divides each vector by its magnitude   
def orthon(dim, vecnum, basis):
    mag = m.sqrt(sum((basis[vecnum,x])**2 for x in range(dim)))
    basis[vecnum,:] = basis[vecnum,:]/mag
        
    
def main():
    dim = int(input("What is the dimension of the vector space? "))
    numOfVecs = int(input("How many vectors are in the basis of the vector space? "))
    basisnums = input("Enter the basis vectors, coordiates and vectors separated by spaces. \nFor example, (1, 0, 0), (0, 1, 0), and (0, 0, 1) would go as 1 0 0 0 1 0 0 0 1:\n")
    # Inital basis vectors
    basisVectors = np.asarray(basisnums.split(" ")).astype(int).reshape(numOfVecs, dim)
    # Final basis vector matrix (empty at first, but gets filled up)
    basisVectorsF = np.empty([numOfVecs, dim], dtype='float')
    for i in range(numOfVecs):
        orthog(i, basisVectors, basisVectorsF)
    for i in range(numOfVecs):
        orthon(dim, i, basisVectorsF)
    print(basisVectorsF)
        

if __name__ == '__main__':
    main()

