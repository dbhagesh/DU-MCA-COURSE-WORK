import numpy as np

r = int(input("Enter number of row: "))
c = int(input("Enter number of column: "))


if r!=c:
    print("Input a square matrix only.")
else:
    print("Input Matrix elements: ")
    mat1 = [[int(input()) for x in range(c)] for y in range(r)]
    sum1=0
    for i in range(r):
        for j in range(c):
            if(i==j):
                sum1+=mat1[i][j]
    
    print("Sum of digonal elements is : ",sum1)