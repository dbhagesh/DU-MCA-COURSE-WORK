d=int(input("Enter the dimension of the vector: "))
print("Input the vector : ")
myList=[int(input()) for x in range(d)]
myList.sort()
print("Min element is: {} and Max element is {} ".format(myList[0],myList[d-1]))