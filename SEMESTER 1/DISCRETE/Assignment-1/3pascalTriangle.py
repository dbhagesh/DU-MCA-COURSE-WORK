'''
3. Write a program to generate a Pascal’s triangle.
'''
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

def combination(n,k):
    return int(fact(n)/(fact(k)*fact(n-k)))

def printPascalTriangle(n):
    space=int((2*n)/2)

    for i in range(1,n+1):
        print((space-i)*" ",end="")
        
        for j in range(i):
            print(combination(i-1,j),end=" ")
        
        print((space-i-1)*" ")
        


def main():
    n=int(input("Enter the number of rows: "))
    printPascalTriangle(n)

if __name__=='__main__':
    main()