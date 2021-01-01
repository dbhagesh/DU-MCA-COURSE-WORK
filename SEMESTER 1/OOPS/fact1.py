'''
Program to calculate factorial of numbers upto n
I/P:
Enter the number upto which we have to prnt factorial : 5
O/P:
Factorial of 1 is : 1
Factorial of 2 is : 2
Factorial of 3 is : 6
Factorial of 4 is : 24
Factorial of 5 is : 120
'''
'''
Main function
Inputs integer 'n'
Calls fact(n) function
'''
def main():
    n=int(input("Enter the number upto which we have to prnt factorial : "))
    fact(n)
'''
Purpose: Recursive function to print factorial of all natural number upto 'n'
Parameters: Integer 'n'
Return: Returns the recursive call of previous natural number and prints the factorial of particular number
'''
def fact(n):
    if n>1:
        #Making recursive call to function for finding factorial
        fac= n*fact(n-1)
        print("Factorial of {} is : {}".format(n,fac))
        return fac
    else:
        #Terminating condition
        print("Factorial of 1 is : 1")
        return 1

if __name__ == "__main__":
    main()