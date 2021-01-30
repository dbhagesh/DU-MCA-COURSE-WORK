'''
Program to count elements in the strung using recursion.
Takes 1 string 'string' as input.
Outputs the count of elements.
I/P:
Enter the string: We all love python.
O.P:
Count is:  4
'''

'''
Function count number of elements in the 'string' using recursion
Parameters: String type 'string'
Return: Returns the count of integer type.
'''
def countEle(string):
    #Terminating condition if len() of string is 0
    if(len(string)==0):
        return 0
    #If we encounter space, increment count
    if(string[0]==' '):
        return 1+countEle(string[1:])
    #Else gives recursive call to next character
    else:
        return countEle(string[1:])
    
'''
Main function for processing the logic of the program
Calling the required functions
And taking inputs from the user
Parameters: None
Return: Nothing, but prints the count.
''' 
def main():
    #Inputting string
    string=input("Enter the string: ")
    #If string is empty
    if(len(string)==0):
        print("String is empty.")
    else:
        #Stripping extra spaces from the input
        string=string.strip()
        #Printing the count
        #Addding 1 because last word wont be counted as there will be no space as its sufix
        print("Count is: ",countEle(string)+1)

#Making main() as driver function
if __name__ == "__main__":
    main()