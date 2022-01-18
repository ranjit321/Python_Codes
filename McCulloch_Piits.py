# define Unit Step Function
def Activation(v):
	if v >= 1:
		return 1
	else:
		return 0

def OR_Model(x1,x2):
    s=x1+x2
    if s>=1:
        return 1
    else:
      return 0   

def OR_3_Model(x1,x2,x3):
    s=x1+x2+x3
    if s>=1:
        return 1
    else:
      return 0 

def AND_Model(x1,x2):
    s=x1+x2
    if s>=2:
        return 1
    else:
      return 0  


def NOT_Model(x):
    if x>=1:
        return 1
    else:
      return 0  

print("OR GATE:")
print("{}, {}= {}".format(0, 0, OR_Model(0,0)))
print("{}, {}= {}".format(0, 1, OR_Model(0,1)))
print("{}, {}= {}".format(1, 0, OR_Model(1,0)))
print("{}, {}= {}".format(1, 1, OR_Model(1,1)))
print()
print("AND GATE:")
print("{}, {}= {}".format(0, 0, AND_Model(0,0)))
print("{}, {}= {}".format(0, 1, AND_Model(0,1)))
print("{}, {}= {}".format(1, 0, AND_Model(1,0)))
print("{}, {}= {}".format(1, 1, AND_Model(1,1)))
print()
print("3 Input OR GATE:")
print("{}, {}, {}= {}".format(0, 0, 0, OR_3_Model(0,0,0)))
print("{}, {}, {}= {}".format(0, 0, 1, OR_3_Model(0,0,1)))
print("{}, {}, {}= {}".format(0, 1, 0, OR_3_Model(0,1,0)))
print("{}, {}, {}= {}".format(0, 1, 1, OR_3_Model(0,1,1)))
print("{}, {}, {}= {}".format(1, 0, 0, OR_3_Model(1,0,0)))
print("{}, {}, {}= {}".format(1, 0, 1, OR_3_Model(1,0,1)))
print("{}, {}, {}= {}".format(1, 1, 0, OR_3_Model(1,1,0)))
print("{}, {}, {}= {}".format(1, 1, 1, OR_3_Model(1,1,1)))


print()
print("NOT(0) = {}".format(NOT_Model(0)))
print("NOT(1) = {}".format(NOT_Model(1)))
