'''
Program to multiply two numbers with recursion.
Takes 2 integers 'num1' and 'num2' as input.
Outputs the product of inputs
I/P:
Enter 1st number: 5
Enter 2nd number: 4
O.P:
PRODUCT:  20
'''
'''
Function to multipy two numbers using recursion
Parameters: Integer type -num1 and num2
Return: Returns the product of integer type.
'''
def multi(num1,num2):
    #Terminating condition
    if(num2==0):
        return 0
    #Returns the sum of num1, num2 times.
    return num1+multi(num1,num2-1)

'''
Main function for processing the logic of the program
Calling the required functions
And taking inputs from the user
Parameters: None
Return: Nothing, but prints the product.
'''
def main():
    #Inputting numbers
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
    #For less computational task passing smaller number as second argument
    if(num1>num2):
        print("PRODUCT: ",multi(num1,num2))
    else:
        print("PRODUCT: ",multi(num2,num1))

#Making main function as driver function
if __name__ == "__main__":
    main()