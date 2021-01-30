'''
Program to flatten the list using recursion.
Outputs the flatten list.

O.P:
Original List:  [1, [2, 3, 4], [5], 6, 7]
Flatted List :  [1, 2, 3, 4, 5, 6, 7]
'''
'''
Function to return the flattned list using recursion
Parameters: list type - myList, copiedList.
Return: Returns the flattened list in the copiedList.
'''
def copyList(myList,copiedList):
    #Terminating condition when myList gets empty
    if(len(myList)==0):
        return 0
    #If nested list is encountered
    if type(myList[0])==type(list()):
        #Appending the nested element
        copiedList.append(myList[0][0])
        #Function called again with the nested list as parameter
        copyList(myList[0][1:],copiedList)
    else:
        #Appends the non nested element
        copiedList.append(myList[0])
        #return copyList(myList[1:],copiedList)
    #Calls function again with myList[1:]
    copyList(myList[1:],copiedList)
'''
Main function is the driver function.
Calls the flatten list function on list
Processes the output after flattening the list

'''
def main():
    #Multi D list
    list1=[1,[2,3,4],[5],6,7]
    #List where the flatten list will be stored
    copiedList=[]
    #Function to flatten the list
    copyList(list1,copiedList)
    print("Original List: ",list1)
    print("Flatted List : ",copiedList)
    

#Making main function as driver function
if __name__ == "__main__":
    main()