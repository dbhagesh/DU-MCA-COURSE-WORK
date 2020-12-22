'''
Given a list of 'n' numbers i.e. 1 to n, print even and odd numbers.
This program takes an integer 'n' as input and prints the odd and even numbers
e.g. 
I/p:Enter 'n' value: 5
O/p:
Odd numbers are:  [1, 3, 5]
Even numbers are:  [2, 4]

'''
#Main function
def main():
    #Inputing the list size
    n=int(input("Enter 'n' value: "))
    #Function to fill the number with natural numbers
    myList=fillList(n)
    #Function to print odd and even numbers out of the list
    oddAndEven(myList,n)

'''
Purpose: Function fill a list of 'n' size
Parameter: Inputted integer 'n'
Return: Filled list with natural numbers 1 to n
'''
def fillList(n):
    #Initialising a list of 'n' size with zeroes 
    #to later modify it according to our need
    myList=[0]*n
    #Filling natural numbers
    for i in range(n):
        myList[i]=i+1
    return myList

'''
Purpose: Function print odd and even numbers present in the list
Parameter: Filled list, Inputted integer 'n'
Return: returns nothing, but prints odd and even numbers
'''
def oddAndEven(myList,n):
    #Empty odd and even list
    oddList=[]
    evenList=[]
    #Checking if the ith value contains odd or even number
    #and later appending odd number in odd list and even in even. 
    for i in range(n):
        if (myList[i])%2==0:
            evenList.append(i+1)
        else:
            oddList.append(i+1)
    print("Odd numbers are: ",oddList)
    print("Even numbers are: ",evenList)

#Assigning the main function as the driver function
if __name__ == "__main__":
    main()