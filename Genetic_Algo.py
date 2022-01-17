import random
import numpy as np

#CFG for greatest of 3 numbers have 5 paths as below: 
#path 1: 1-2-3-4-11 means (a>b) and (b>c) 
#path 2: 1-2-3-5-6-11 means (a>b) and (a>c) 
#path 3: 1-2-3-5-7-11 means (a>b) and (c>a) 
#path 4 :1-2-8-9-11 means (b>a) and (c>b) 
#path 5: 1-2-8-10-11 means (b>a) and (c>b) 

#function to conver Decimal to 8 bit binary number
def decimalToBinary(n):
    binary = bin(n).replace('0b','')
    x = binary[::-1] #this reverses an array.
    while len(x) < 8:
        x+='0'
        binary=x[::-1]
    return binary 

#perform cross over on 8 bit representaion of 3 numbers
def crossover(l1,l2,l3):
    l1=list(l1)
    l2=list(l2)
    l3=list(l3)

    for i in range(3,6):
         l1[i],l2[i]=l2[i],l1[i]
    for j in range(6,9):
         l2[j],l3[j]=l3[j],l2[j]
    a=''.join(l1)
    b=''.join(l1)
    c=''.join(l3)

    return int(a,2),int(b,2),int(c,2)

def mutation(x): # mutate the 5th bit given number
        p=[]
        for bit in range(len(x)):
             m=x[bit]
             p.append(m)

        p[4] = '1' if p[4] == '0' else '0'
        b=p[0] + p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
        x=b   
                 
        return int(x,2)
        
P=int(input("enter population size: "))
T=int(input("enter test suite size: "))

Population=[[[0 for k in range(3)] for j in range(T)] for i in range(P)]


for i in range(0,P):
    for j in range(0,T):
        for k in range(0,3):
            Population[i][j][k]=random.randrange(-5,5)


def printPopulation():

    for i in range(0,P):
        print("Chromosome No:",i+1)
        print("\n")
        for j in range(0,T):
            print(Population[i][j])
        print("\n")



pathcoverage=0
sat_flag=[0,0,0,0] #flags to check which chromosome satisfied
percentage_path=[0,0,0,0]
for it in range(0,10): #number of iteraions
    print("\n")
    print("Iteration No:",it+1)
    print("\n\n")
    printPopulation()
    for i in range(0,P):
        if(sat_flag[i]!=1):
            #print("Suite No:",i+1)
            paths=[0,0,0,0,0]
           # if( not sat_flag[i]):
            for j in range(0,T):
                    a=Population[i][j][0]    
                    b=Population[i][j][1]
                    c=Population[i][j][2]
                    if (a>b):
                     if(b>c):
                        paths[0]+=1
                     elif (a>c):
                        paths[1]+=1
                     else:
                        paths[2]+=1    
                    elif (b>c):
                     paths[3]+=1
                    else:
                     paths[4]+=1


            paths_covered=np.count_nonzero(paths)
            percentage_path[i]=(paths_covered/5)*100

     
    for i in range(0,P):
        print("Chromosome No.",i+1)
        print("path coverage percentage",percentage_path[i])

    for i in range(0,P):
        if(percentage_path[i]<60): #crosss over
            for j in range(0,5):
                l1=decimalToBinary(Population[i][j][0])
                l2=decimalToBinary(Population[i][j][1])
                l3=decimalToBinary(Population[i][j][2])
                Population[i][j][0],Population[i][j][1],Population[i][j][2]=crossover(l1,l2,l3)

        elif percentage_path[i]>60 and percentage_path[i]<80: #Next step mutation
            for j in range (0,5):
                l4=decimalToBinary(Population[i][j][1])
                Population[i][j][1]=mutation(l4)
        else: #satisfied , so no cross over 0r mutation required
            sat_flag[i]=1

             

  
    
        




               
  
