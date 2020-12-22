#Main Function
def main():
    listL=int(input("Enter number of elements to be present in the list: "))
    
    myList=inputList(listL)
    cumSum(myList,listL)
    
#Function to input values in the list
#Parameters: Length of list:int value
def inputList(listL):
    myList=[0]*listL
    for i in range(listL):
        myList[i]=int(input("Enter {} element:".format(i+1)))
    return myList
#Function to print cumulative sum of a user list
#Parameters: User input list, User length of list
def cumSum(myList,listL):
    newMyList=[]
    for i in range(listL):
        newMyList.append(sum(myList[:i+1]))
    print("Original: ",myList)
    print("Cumulative :",newMyList)

if __name__ == "__main__":
    main()

