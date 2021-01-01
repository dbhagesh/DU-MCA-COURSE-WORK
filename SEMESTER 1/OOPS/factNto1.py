'''
Program to calculate factorial of numbers upto n
I/P:
Enter the number upto which we have to prnt factorial : 5
O/P:
Factorial of 0 is : 120
Factorial of 1 is : 24
Factorial of 2 is : 6
Factorial of 3 is : 2
Factorial of 4 is : 1
'''
'''
Main function
Inputs integer 'n'
Calls fact(n) function and prints the list factorial in decreasing order
'''
def main():
    n=int(input("Enter the number upto which we have to prnt factorial : "))
    global myList
    myList=[]
    fact(n)
    
    for i,j in zip(myList[::-1],range(n)):
        print("Factorial of {} is : {}".format(j,i))
'''
Purpose: Recursive function to print factorial of all natural number upto 'n'
Parameters: Integer 'n'
Return: Returns the recursive call of previous natural number and prints the factorial of particular number
'''
def fact(n):
    if n>1:
        #Making recursive call to function for finding factorial
        fac= n*fact(n-1)
        myList.append(fac)
        #print("Factorial of {} is : {}".format(n,fac))
        return fac
    else:
        #Terminating condition
        #print("Factorial of 1 is : 1")
        myList.append(1)
        return 1

if __name__ == "__main__":
    main()