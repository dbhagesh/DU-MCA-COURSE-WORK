'''
Program to shallow copy the 1D or 2 D list using recursion .

Outputs: Shallow Copied lists of 1D and 2D lists

O.P:
Changing the nested element to 9 and it reflected back in both lists.
Multi D before            :  [1, 2, [9, 4], 5, [6, 7]]
Multi D after shallow copy:  [1, 2, [9, 4], 5, [6, 7]]
Changing non nested element and it wont reflect in the copied list.
1 D before            :  [9, 2, 3, 4, 5]
1 D after shallow copy:  [1, 2, 3, 4, 5]

'''
'''
Function to shallowcopy the lists
Parameters: list type -'list1', 'list2'
Return: Returns the shallow copied list.
'''
def shallowcopy(list1,list2):
    #Terminating condition when the list gets empty
    if(len(list1)==0):
        return 0
    #Appending the first element of list1 to list2
    list2.append(list1[0])
    #Calling the function again with list1[1:],list2
    return shallowcopy(list1[1:],list2)
'''
Main function is the driver function.
Calls the shallowcopy function on both the lists
Processes the output after shallowcopy on 1D and 2D lists

'''
def main():
    #Multi D list
    listnD=[1,2,[3,4],5,[6,7]]
    #1 D List
    list1D=[1,2,3,4,5]
    #Storing the list after copying
    copied1DList=[]
    copiednDList=[]
    
    
    #Functions to shallowcopy
    shallowcopy(list1D,copied1DList)
    shallowcopy(listnD,copiednDList)
    #Changing element inside the list
    #It wont reflect back in the shallowcopied list
    list1D[0]=9
    #Changing element of the nested list
    #It will reflect back in the shallowcopied list 
    listnD[2][0]=9
    print("Changing the nested element to 9 and it reflected back in both lists.")
    print("Multi D before            : ",listnD)
    print("Multi D after shallow copy: ",copiednDList)

    print("Changing non nested element and it wont reflect in the copied list.")
    print("1 D before            : ",list1D)
    print("1 D after shallow copy: ",copied1DList)

#Making main() as driver function
if __name__ == "__main__":
    main()