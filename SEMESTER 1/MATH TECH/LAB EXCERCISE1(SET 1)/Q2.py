import numpy as np

r = int(input("Enter number of row: "))
c = int(input("Enter number of column: "))


if r!=c:
    print("Input a square matrix only.")
else:
    print("Input Matrix elements: ")
    mat1 = [[int(input()) for x in range(c)] for y in range(r)]
    mat = np.trace(mat1)
    print("Sum of digonal elements is : ",mat)