def main():
    print("Main function")
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    c=int(input("Enter second number"))    
    comp3(a,b,c)

def comp3(a,b,c):
    if((a==b)&&(b==c)):
            print("All numbers equal")
    elif(a>b):
        if(a>c):
            print("a is greatest")
        else:
            print("c is greatest")
    elif(b>a):
        if(b>c):
            print("b is greatest")
        else:
            print("c is greatest")
    

if(__name__=='__main__'):
    main()
    
