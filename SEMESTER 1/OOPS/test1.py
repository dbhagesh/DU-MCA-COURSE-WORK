'''
Given a list of 'n' numbers i.e. 1 to n, print prime numbers and total numbers of prime number
e.g.
I/p:Enter number upto which we have to find prime numbers:20
o/p: 
2,3,5,7,11,13,17,19,
Total numbers of prime from 1 to 20 are: 8
'''
#Main function
def main():
    c=0 # Count of prime numbers
    n=int(input("Enter number upto which we have to find prime numbers:")) # Inputing a number 
    #Finding prime numbers upto n natural numbers
    #Running range from 2 because 1 is non prime we already know
    for i in range(2,n+1):
        if(checkPrime(i)!=1):
            c+=1#Increasing count if number is prime
            print(i,end=",")
    print("\nTotal numbers of prime from 1 to {} are: {} ".format(n,c))

'''
Purpose: Function to check if a number is prime or not
Parameter: Integer 'i' i.e a number.
Return: returns 1 if  non prime and returns nothing if prime
'''
def checkPrime(i):
    #Checking if number 'i' is divisible at any momment to 'j'
    for j in range(2,int(i/2)+1):
        #If i is divisible by j
        if(i%j==0):
            return 1

#Making main function as driver function
if __name__ == "__main__":
    main()