# using numpy for array

# Single-dimensional Array

import numpy as np

contain = [10,20,30]
n1= np.array(contain)
print(type(n1))
print(n1)

# Multi-dimensional Array

holder = [[10,20,30],[1,2,3]]
n1 = np.array(holder)
print(type(n1))
print(n1)

# Different ways of initializing numpy array

# initializing zeros
n1 = np.zeros((1,2)) # enter the dimensions
print(n1)
n1 = np.zeros((5,5))
print(n1)

# initializing array with same numbers
n1 = np.full((3,3),1)
print(n1)

#initializing array in certain range and with a certain difference
n1 = np.arange(10,20)
print(n1)
n1 = np.arange(10,50,5)
print(n1)

# initializing array with random numbers
n1 = np.random.randint(1,130,5)
print(n1)

# getting the shape or dimensions of an array
n1 = np.array([[1,2,3],[3,4,5]])
print(n1.shape)
# also used to reshape and resize the array
n1.shape = (3,2)
print(n1)

# using stack for array
n1 = np.array([1,2,3])
n2 = np.array([6,5,4])

# using vstack
print(np.vstack((n2,n1)))

#using hstack
print(np.hstack((n2,n1)))

#using column stack
print(np.column_stack((n2,n1)))

# using special operations
n1 = np.array([1,2,3])
n2 = np.array([6,5,4,1])
# intersection of both array
print(np.intersect1d(n1,n2))

# find unique value of the first array
print(np.setdiff1d(n1,n2)) # 2,3

print(np.setdiff1d(n2,n1)) # 4,5,6

# Addition of numpy array

n10 = np.array([10,20])
n20 = np.array([89,90])
print(np.sum([n10,n20]))

# sum along row and column using axis
print(np.sum([n10, n20], axis=0))

#sum along column using axis
print(np.sum([n10,n20], axis=1))

#using basic scalar operation
n34 = np.array([12,23,34,45])
n34 = n34 + 1
print(n34)
n34 = n34-1
print(n34)
n34 = n34 * 2
print(n34)
n34 = n34/2
print(n34)



