'''
This program take a string input 's' to print its reverse
e.g:
I/P:Enter the string to reverse it:-Bhagesh
O/P:hsegahB
'''
#Main Function: Driver function
def main():
    s=input("Enter the string to reverse it:-")
    print(revStr(s))
'''
Function to reverse string using slicing
Purpose: Rversing a string
Parameter: Inputted string 's'
Return: The reversed string
'''
def revStr(s):
    return s[::-1]

#Making main() as driver function
if __name__ == "__main__":
    main()

