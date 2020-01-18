import numpy as np
import math as m
from fractions import Fraction
# np.set_printoptions(formatter={'all':lambda x: str(Fraction(x).limit_denominator())})

def inner(v1, v2):
    return np.dot(v1, v2)

def proj(v1, v2):
    return (inner(v1, v2)/inner(v2, v2))*v2
    
def orthog(vecnum, ibasis, fbasis):
    if vecnum == 0:
        fbasis[0,:] = ibasis[0,:]
    if vecnum != 0:
        fbasis[vecnum,:] = ibasis[vecnum,:] - sum(proj(ibasis[vecnum,:], fbasis[x,:]) for x in range(vecnum))
    
def orthon(dim, vecnum, basis):
    mag = m.sqrt(sum((basis[vecnum,x])**2 for x in range(dim)))
    basis[vecnum,:] = basis[vecnum,:]/mag
        
    
def main():
    dim = int(input("What is the dimension of the vector space? "))
    basisnums = input("Enter the basis vectors, coordiates and vectors separated by spaces. \nFor example, (1, 0, 0), (0, 1, 0), and (0, 0, 1) would go as 1 0 0 0 1 0 0 0 1:\n")
    basisVectors = np.asarray(basisnums.split(" ")).astype(int).reshape(dim, dim)
    basisVectorsF = np.empty([dim, dim], dtype='float')
    for i in range(dim):
        orthog(i, basisVectors, basisVectorsF)
    for i in range(dim):
        orthon(dim, i, basisVectorsF)
    print(basisVectorsF)
        

if __name__ == '__main__':
    main()

