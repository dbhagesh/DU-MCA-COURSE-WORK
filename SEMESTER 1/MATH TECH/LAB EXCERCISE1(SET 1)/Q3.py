import numpy as np

r = int(input("Enter number of row: "))
c = int(input("Enter number of column: "))



print("Input Matrix 1 elements: ")
mat1 = [[int(input()) for x in range(c)] for y in range(r)]
print("Input Matrix 2 elements: ")
mat2 = [[int(input()) for x in range(c)] for y in range(r)]
print("Matrix 1: ",mat1)
print("Matrix 2: ",mat2)

mat = [[0 for i in range(c)] for j in range(r)]
print(mat)
for i in range(r):
    for j in range(c):
        mat[i][j]=mat1[i][j]*mat2[i][j]

print("After element wise matrix multiplication:")
print(mat)