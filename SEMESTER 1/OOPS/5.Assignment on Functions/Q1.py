'''
Find the sum of squares of individual digits of a number 'sqdnumber' and
 store the sum in variable 'sqdNumber_result'.
 E.g. if the number is 234, the sum is computed as (2^2 + 3^2 + 4^2 = 4 + 9 + 16 = 29) 
I/P:
Enter number: 346
O/P:
Required sum is :  61
'''

'''
Purpose: Main function i.e driver function
It inputs 'sqdNumber' from user and contain the required function calls.
It prints the 'sqdNumber_result'
'''
def main():
    #User inputted number
    sqdnumber=int(input("Enter number: "))
    #Required result
    sqdNumber_result=sqFunc(sqdnumber)
    print("Required sum is : ",sqdNumber_result)

'''
Purpose:Function to return the sum of squares of each digits of the number
Parameters: Integer 'sqdnumber'
Return: Returns the sum of squares of each digit of 'sqdnumber'
'''
def sqFunc(sqdnumber):
    #Variable to store sum
    mySum=0
    #Processing the individual digits by squaring each digits and adding them to 'mySum'
    while(sqdnumber>0):
        mySum+=(sqdnumber%10)**2
        sqdnumber=int(sqdnumber/10)
    return mySum

#Makes main function as the driver function
if __name__ == "__main__":
    main()
