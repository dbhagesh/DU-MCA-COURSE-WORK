'''
Take 'n' numbers from the user and a number 'm'. Find all possible pairs of numbers form inputted 'n' numbers that sum up to m
This program takes an integer 'n','m' as input and prints the pairs that sum to 'm'.
e.g. 
I/p:
Enter 'n' value: 5
Enter 'm' value: 3
Enter 1 value: 1
Enter 2 value: 2
Enter 3 value: 3
Enter 4 value: 4
Enter 5 value: 5
O/p:
[1,2]

'''
#Main function
def main():
    #'n' is list size
    n=int(input("Enter 'n' value: "))
    #'m' is the sum of pairs
    m=int(input("Enter 'm' value: "))
    #Function to fil list with user input
    myList=fillList(n)
    #Function to print the existing pairs
    findPairs(myList,n,m)

'''
Purpose: Function fill a list of 'n' size with user input
Parameter: Inputted integer 'n'
Return: Filled list with user inputed values
'''
def fillList(n):
    #Initialising a list of 'n' size with zeroes 
    #to later modify it according to our need
    myList=[0]*n
    for i in range(n):
        myList[i]=int(input("Enter {} value: ".format(i+1)))
    return myList

'''
Purpose: Function print pairs which sum upto 'm'
Parameter: Filled list and inputted integer 'n','m'.
Return: returns nothing, but prints the pairs
'''
def findPairs(myList,n,m):
    #Traversing the list to find the pairs
    for i in range(n):
        for j in range(i,n):
            temp=[]
            if myList[i]+myList[j]==m:
                temp=[myList[i],myList[j]]
                print(temp)

#Assigning the main function as the driver function
if __name__ == "__main__":
    main()