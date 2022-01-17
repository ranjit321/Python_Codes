#Program 2: Python program to find eigen values of given matrices
import numpy as np
from numpy.linalg import eig

def getEigen(mat):
    arr=np.array(mat)
    values,vectors=eig(arr)
    print(values.astype(int))


if __name__=='__main__':


    mat1=[[1,2],
          [2,4]]
    mat2=[[0,-1,-1],
          [-6,-11,6],
          [-6,-11,5]]
    print("eigen values of matrix 1 are:")
    getEigen(mat1)
    print("eigen values of matrix 2 are:")
    getEigen(mat2)
    
    
