'''
Program to reverse the string using recursion.
Takes 1 string 'string' as input.
Outputs the count of elements.
I/P:
Enter the string: bhagesh is good boy
O.P:
Reverse of String:  yob doog si hsegahb
'''

'''
Function to return reverse of 'string' using recursion
Parameters: String type 'string'
Return: Returns the reversed 'string' of string type.
'''
def revStr(string):
    #Terminating condition when string is empty
    if(len(string)==0):
        return ""
    #Returns the last word and call to revStr(string without last character)
    return string[-1]+revStr(string[:len(string)-1])
'''
Main function for processing the logic of the program
Calling the required functions
And taking inputs from the user
Parameters: None
Return: Nothing, but prints the reverse of 'string'.
''' 
def main():
    #Inputting string
    string=input("Enter the string: ")
    #If string is empty
    if(len(string)==0):
        print("String is empty.")
    else:
        #Stripping extra spaces from both ends
        string=string.strip()
        #Printing returned string from revStr()
        print("Reverse of String: ",revStr(string))
        
#Making main() as driver function
if __name__ == "__main__":
    main()