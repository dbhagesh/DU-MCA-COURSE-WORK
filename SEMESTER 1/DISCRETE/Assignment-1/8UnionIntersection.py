def main():
    n1=int(input("Enter the number of elements in set A: "))
    n2=int(input("Enter the number of elements in set B: "))
    A=set()
    B=set()
    #Inputing set A
    for i in range(n1):
        A.add(input("Enter element set A: "))
    #Inputing set A
    for i in range(n2):
        B.add(input("Enter element set B: "))
    
    #If intersection/union is empty
    if((A&B)==set()):
        print("INTERSECTION IS EMPTY")
    else:    
        print("INTERSECTION : ",A & B)
    
    if((A | B)==set()):
        print("UNION IS EMPTY")
    else:
        print("UNION : ",A | B)
        
if __name__=='__main__':
    main()
