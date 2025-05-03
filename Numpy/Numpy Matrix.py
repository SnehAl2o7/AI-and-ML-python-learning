import numpy as np

n1 = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(n1)
#to represent the row
print(n1[0])
#to print a particular element, row etc
print(n1[1:2,2])

#transpase
np.transpose(n1)
print(n1)

#using dot product to multiply matrixs
n2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
n1 = np.array([[9,8,7],[6,5,4],[3,2,1]])

print(n1.dot(n2))

# save and load an array
np.save('my_numpy',n1)
n45 = np.load('my_numpy.npy')
print(n45)