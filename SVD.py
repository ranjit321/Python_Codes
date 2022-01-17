
#Program 4: Python program to find SVD of given matrix
import numpy as np

def getSVD(mat):
    U,S,VT=np.linalg.svd(mat)
    print("Singular value decomposition:")
    print("U\n",U)
    print("Sigma\n",S)
    print("VT\n",VT)



if __name__=='__main__':


    mat=[[3,1,0],
          [1,2,2],
          [0,1,1]]
    getSVD(mat)
