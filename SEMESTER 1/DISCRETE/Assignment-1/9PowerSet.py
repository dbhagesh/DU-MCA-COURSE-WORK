'''
9. Write a program to find the power set of the given set.
'''
def powerset(s):
    power=[[]]
    
    for ele in s:
        for sub in power:
            power=power+[list(sub)+[ele]]
    return power


            
def main():
    n1=int(input("Enter the number of elements in the set : "))
    A=set()
    for i in range(n1):
        A.add(input("Enter element {} of the set : ".format(i+1)))
    
    powerlist=powerset(list(A))
    print("Power set is : ")
    for i in powerlist:
        print(i)

if __name__=='__main__':
    main()