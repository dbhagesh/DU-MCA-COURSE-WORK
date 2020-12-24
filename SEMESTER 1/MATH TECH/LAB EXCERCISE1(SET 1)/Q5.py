import numpy as np

s = int(input("Enter size of square matrix "))

print("Input Matrix elements: ")
mat1 = ([[int(input()) for x in range(s)] for y in range(s)])
print(mat1)
mat = np.linalg.det(mat1)
print("Determinent is : ",mat)