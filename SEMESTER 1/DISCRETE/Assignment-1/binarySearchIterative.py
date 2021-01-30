'''
1. Write a program to implement Binary search (Iterative).
'''
def binary_search(array,ele):
    l=0
    r=len(array)-1
    while(l<=r):
        
        mid=int((l+r)/2)
        if(array[mid]==ele):
            print("Element found")
            return
        elif ele>array[mid]:
            l=mid+1
        elif ele<array[mid]:
            r=mid-1
        print("L:",l,"-R:",r)
    print("Element not found.")
    return
        

    
        
def main():
    n=int(input("Enter length of the array: "))
    array=[int(input()) for x in range(n)]
    print("Array before sorting: ",array)
    ele=int(input("Enter element to search: "))
    binary_search(array,ele)

if __name__ == "__main__":
    main()