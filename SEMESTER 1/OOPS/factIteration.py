'''
Program to print factorial of natural numbers upto n.
Example-
I/P: 
Enter n upto which you want to print factorials : 5
O/P:
Factorial of 1 is 1
Factorial of 2 is 2
Factorial of 3 is 6
Factorial of 4 is 24
Factorial of 5 is 120
'''
'''
Main function
Inputs integer 'n'
Calls factI(n) function
'''
def main():
    n=int(input("Enter n upto which you want to print factorials : "))
    #Calling iterating function for finding factorial
    factI(n)
'''
Purpose: Function to print factorial of numbers upto n by iterative method
Parameters: Integer 'n'
Returns: Returns nothing but prints the factorial of numbers upto n
'''
def factI(n):
    for i in range(1,n+1):
        #Variable to store factorial of natural numbers
        fac=1
        for j in range(1,i+1):
            #Calculating factorial
            fac*=j
        print("Factorial of {} is {} ".format(i,fac))

#Making main function as driver function
if __name__ == "__main__":
    main()