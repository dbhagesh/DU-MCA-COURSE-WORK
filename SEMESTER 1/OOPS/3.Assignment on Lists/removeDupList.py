#Main Function
def main():
    listL=int(input("Enter number of elements to be present in the list: "))
    myList=inputList(listL)
    removeDuplicate(myList,listL)
    
#Function to input values in the list
#Parameters: Length of list:int value

def inputList(listL):
    #A empty list of user size
    myList=[0]*listL
    for i in range(listL):
        myList[i]=input("Enter {} element:".format(i+1))
    return myList

#Function to remove duplicate values
#Parameters: User input list, User length of list
def removeDuplicate(myList,listL):
    newMyList=[] #New list
    for item in myList:
        if item not in newMyList:
            newMyList.append(item)
    print(newMyList)

if __name__ == "__main__":
    main()