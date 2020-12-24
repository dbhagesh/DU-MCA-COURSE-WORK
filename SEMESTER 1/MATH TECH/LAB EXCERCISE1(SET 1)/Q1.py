import numpy as np

r1 = int(input("Enter number of row: "))
c1 = int(input("Enter number of column: "))
r2 = int(input("Enter number of row: "))
c2 = int(input("Enter number of column: "))

if c1!=r2:
    print("Input multiplication friendly matrix sizes i.e c1=r2")
else:
    print("Input Matrix 1 elements: ")
    mat1 = [[int(input()) for x in range(c1)] for y in range(r1)]
    print("Input Matrix 2 elements: ")
    mat2 = [[int(input()) for x in range(c2)] for y in range(r2)]
    print("Matrix 1: ",mat1)
    print("Matrix 2: ",mat2)
    mat = np.dot(mat1,mat2)
    print("After matrix multiplication:")
    print(mat)