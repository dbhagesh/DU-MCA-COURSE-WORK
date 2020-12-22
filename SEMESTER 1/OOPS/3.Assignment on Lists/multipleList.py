#Main Function
def main():
    listL=int(input("Enter number of elements to be present in the list: "))
    
    myList=inputList(listL)
    multipleList(myList,listL)
    
#Function to input values in the list
#Parameters: Length of list:int value
def inputList(listL):
    myList=[0]*listL
    for i in range(listL):
        myList[i]=int(input("Enter {} element:".format(i+1)))
    return myList
#Function to print multi-dim list which contains first five multiples of ith value of list
#Parameters: User input list, User length of list
def multipleList(myList,listL):
    newMyList=[]
    for i in range(listL):
        temp=[]
        for j in range(1,6):
            temp.append(myList[i]*j)
        newMyList.append(temp)
    print("Original: ",myList)
    print("Cumulative :",newMyList)

if __name__ == "__main__":
    main()

