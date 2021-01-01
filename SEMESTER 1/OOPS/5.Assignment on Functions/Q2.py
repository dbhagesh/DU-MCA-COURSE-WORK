'''
Happy Numbers: A number is called a happy number, if you repeat the process,
of squaring the sum of the digits, till the value 1 is obtained. E.g. You
need to do the following to perform this check: (a) compute the sum of the
squares of its digits (b) if the resultant value is 1, then the number is
a happy number, else execute point (a). If a number is not a happy number,
there will be an endless loop/cycle to this execution. 

You are required to write code that checks whether the number is a happy number
or not, for 10 cycles (iterations) only.
I/P:
Enter number: 70
O/P:
Happy Number
'''

'''
Purpose: Main function i.e driver function
It inputs 'sqdNumber' from user and contain the required function calls.
It prints whether number is Happy Number or Not Happy Number
'''
def main():
    #User inputted number
    sqdnumber=int(input("Enter number: "))
    #Iterates 10 times to check for happy number
    for i in range(10):
        if(sqFunc(sqdnumber)==1):
            #If found happy number returns True
            print("Happy Number")
            return 1
        else:
            #else calculates the sqFunc of that number again
            sqdnumber=sqFunc(sqdnumber)
    print("Not Happy Number")

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
