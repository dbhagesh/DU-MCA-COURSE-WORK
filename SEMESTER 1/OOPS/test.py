import numpy as np
mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3]) 
mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7]) 
  
# This will return dot product 
res = np.dot(mat1,mat2) #mat1@mat2
diagonalSum=np.trace(res)

  
# print resulted matrix 
print(res) 
print(diagonalSum)