'''
10. Write a program to find the permutation of the given set.
'''
def permutations(A):
    if(len(A)==1):
        return [A]
    perm=[]
    
    for i in range(len(A)):
        m = A[i]
        
        remList=A[:i] + A[i+1:]
        
        for p in permutations(remList):
            perm.append([m]+p)
    return perm
    

def main():
    n1=int(input("Enter the number of elements in the set : "))
    A=set()
    for i in range(n1):
        A.add(input("Enter element {} of the set : ".format(i+1)))
    
    for p in permutations(list(A)):
        print(p)
    

if __name__=='__main__':
    main()