import numpy as np

r1 = int(input("Enter number of row: "))
c1 = int(input("Enter number of column: "))
r2 = int(input("Enter number of row: "))
c2 = int(input("Enter number of column: "))


print("Input Vector 1 elements: ")
vector1 = np.array([[int(input()) for x in range(c1)] for y in range(r1)])
print("Input Vector 2 elements: ")
vector2 = np.array([[int(input()) for x in range(c2)] for y in range(r2)])
print("Vector 1: \n",vector1)
print("Vector 2: \n",vector2)
mat = np.outer(vector1,vector2) # or just use mat1*mat2
print("After outer vector multiplication:")
print(mat)