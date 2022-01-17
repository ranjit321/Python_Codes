#Prohram 3: Find largest subsquare matrix containing one 1's

def printMaxSubSquare(Mat):
        R = len(Mat) #number of rows
        C = len(Mat[0]) #number of columns
        Sub = [[0 for n in range(C)] for m in range(R)]
        #initialize the matri with 0

        # Construct other entries
        for i in range(0, R):
                for j in range(0, C):
                        if (Mat[i][j] == 1):
                                Sub[i][j] = min(Sub[i][j-1], Sub[i-1][j],
                                                Sub[i-1][j-1]) + 1
                                
                                
                        else:
                                Sub[i][j] = 0
        
        # Find the maximum entry and
        # indices of maximum entry in Sub[][] matrix
        max_s = Sub[0][0]
        max_i = 0
        max_j = 0
        for i in range(R):
                for j in range(C):
                        if (max_s < Sub[i][j]):
                                max_s = Sub[i][j]
                                max_i = i
                                max_j = j
                        
        print("Largest sub square matrix containing only 1's is:")
        for i in range(max_i, max_i - max_s, -1):
                for j in range(max_j, max_j - max_s, -1):
                        print (Mat[i][j], end = " ")
                print("")

if __name__ == '__main__':
        
    Mat = [ [1, 1, 1, 1, 1],
          [1, 1, 1, 0, 0],
          [1, 1, 1, 0, 0],
          [1, 1, 1, 0, 0],
        [ 1, 1, 1, 1, 1]]

    printMaxSubSquare(Mat)


