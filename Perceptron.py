#OR,AND and OR Gate implementation using perceptron model
import numpy as np

# define Unit Step Function
def unitStep(v):
	if v >= 0:
		return 1
	else:
		return 0

#  Perceptron Model
def perceptron(x, w, b):
	v = np.dot(w, x) + b
	y = unitStep(v)
	return y


def OR_logicFunction(x):
	w = np.array([1, 1])
	b = -0.5
	return perceptron(x, w, b)

def AND_logicFunction(x):
	w = np.array([1, 1])
	b = -1.5
	return perceptron(x, w, b)	

def NOT_logicFunction(x):
	w = -1
	b = 0.5
	return perceptron(x, w, b)	

# testing the Perceptron Model
test1 = np.array([0, 1])
test2 = np.array([1, 1])
test3 = np.array([0, 0])
test4 = np.array([1, 0])

print("OR GATE:")
print("{}, {}= {}".format(0, 1, OR_logicFunction(test1)))
print("{}, {}= {}".format(1, 1, OR_logicFunction(test2)))
print("{}, {}= {}".format(0, 0, OR_logicFunction(test3)))
print("{}, {}= {}".format(1, 0, OR_logicFunction(test4)))
print()
print("AND GATE:")
print("{}, {}= {}".format(0, 1, AND_logicFunction(test1)))
print("{}, {}= {}".format(1, 1, AND_logicFunction(test2)))
print("{}, {}= {}".format(0, 0, AND_logicFunction(test3)))
print("{}, {}= {}".format(1, 0, AND_logicFunction(test4)))

print()
print("NOT(0) = {}".format(NOT_logicFunction(0)))
print("NOT(1) = {}".format(NOT_logicFunction(1)))
