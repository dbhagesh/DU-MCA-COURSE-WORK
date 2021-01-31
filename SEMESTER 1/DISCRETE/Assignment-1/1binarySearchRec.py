'''
1. Write a program to implement Binary search (Recursive).
'''
def binary_search(array,ele):
    size = len(array)
    mid=int(size/2)
    if size==0:
        print("Element not found.")
        return
    elif ele==array[mid]:
        print("Element found.")
        return 
    elif ele<array[mid]:
        return binary_search(array[:mid],ele)
    elif ele>array[mid]:
        return binary_search(array[mid+1:],ele)
    
        
def main():
    n=int(input("Enter length of the array: "))
    array=[int(input()) for x in range(n)]
    print("Array before sorting: ",array)
    ele=int(input("Enter element to search: "))
    binary_search(array,ele)

if __name__ == "__main__":
    main()