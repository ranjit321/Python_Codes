
#Program 1: To find determinant and trace of the given matrix

# return minor matrix after excluding
# i-th row and j-th column.
def getcofactor(m, i, j):
	return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]


#function to get trace of the matrix
def getTrace(mat):
        Sum=0
        for i in range(len(mat)):
                Sum+=mat[i][i]
        return Sum        
#function to get determinnat of the matrix
def determinantOfMatrix(mat):

	if(len(mat) == 2):
		value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
		return value

	Sum = 0

	for j in range(len(mat)):

		# sign corresponding
		# to co-factor of that sub matrix.
		sign = (-1) ** (j)


		sub_det = determinantOfMatrix(getcofactor(mat, 0, j))

		Sum += (sign * mat[0][j] * sub_det)

	return Sum


if __name__ == '__main__':

	mat = [[ 1, 2, 3, 4,1 ],
		[0, -1,2,4, 2 ],
		[0, 0, 4, 0,0 ],
		[-3, -6, -9, -12,4],
		[0, 0, 1, 1,1 ]];

	print('Determinant of the matrix is :', determinantOfMatrix(mat))
	print('Determinant of the matrix is :', getTrace(mat))

