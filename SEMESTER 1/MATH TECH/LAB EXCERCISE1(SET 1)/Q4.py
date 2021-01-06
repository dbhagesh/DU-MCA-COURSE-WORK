'''
As we know vectors are single dimension arrays
So, taking 1st vector as Nx1 and 2nd vector as 1xM matrix
And outer product results in NxM matrix
'''
d1 = int(input("Enter dimension of vector1: "))
d2 = int(input("Enter dimension of vector2: "))

print("Input Vector 1 elements: ")
vector1 = [[int(input()) for x in range(1)] for y in range(d1)]
print("Input Vector 2 elements: ")
vector2 = [[int(input()) for x in range(d2)] for y in range(1)]
print("Vector 1: \n",vector1)
print("Vector 2: \n",vector2)
mat = [[0 for i in range(d2)] for j in range(d1)]
for i in range(d1):
    for j in range(d2):
        for k in range(1):
            mat[i][j]+=vector1[i][k]*vector2[k][j]
print("After outer vector multiplication:")
print(mat)