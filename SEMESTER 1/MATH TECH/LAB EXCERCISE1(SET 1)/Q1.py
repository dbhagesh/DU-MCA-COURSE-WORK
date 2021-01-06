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
    
    mat = [[0 for i in range(c2)] for j in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                mat[i][j]+=mat1[i][k]*mat2[k][j]
    print("After matrix multiplication:")
    print(mat)