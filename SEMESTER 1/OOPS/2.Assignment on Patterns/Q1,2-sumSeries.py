'''
This program take a integer inputs 'n1','n2','x1','x2' to print the sum of series 1 and 2
e.g:
I/P:
Enter 'n' value for first series :10
Enter 'x' value for first series :1
Enter 'n' value for second series :100
Enter 'x' value for second series :1
O/P:
Sum of First series:  0.5403023058681397
---------------------------
Sum of Second series:  2.7182818284590455
'''
#Function to find factorial

'''
Function to find factorial
Purpose: finding factorial
Parameter: integer 'n'
Return: factorial of a number
'''
def fact(n):
    if(n==0):
        return 1
    elif(n!=1):
        return n*fact(n-1)
    elif(n==1):
        return 1
#Main Function    
def main():

    print("'n' is number of terms")
    print("'x' is value of x in exprs.")
    n1=int(input("Enter 'n' value for first series :"))
    x1=int(input("Enter 'x' value for first series :"))
    n2=int(input("Enter 'n' value for second series :"))
    x2=int(input("Enter 'x' value for second series :"))
    sumSeries(n1,x1,n2,x2)


'''
Function to find sum of series
Purpose: finding sum of the series given in question
Parameter: Inputted string 'n1','n2','x1','x2'
Return: Nothing, but prints the sum of both series
'''
def sumSeries(n1,x1,n2,x2):
    sum=0 #Sum of series
    sign=1 #Flag bit for sign
    
    #Sum of first series
    for i in range(n1):
        z=i*2
        sum+=sign*((x1**z)/fact(z))
        sign=sign*-1
    
    print("Sum of First series: ",sum)
    print("---------------------------")
    #Sum of second series
    sum=0
    for i in range(n2):
        sum+=(x2**i)/fact(i) 
    print("Sum of Second series: ",sum)

#Making main() as driver function
if __name__ == "__main__":
    main()