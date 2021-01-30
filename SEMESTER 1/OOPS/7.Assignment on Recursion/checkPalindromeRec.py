'''
Program to check if the input is palindrome or not using recursion.
Takes 1 String 'string' as input.
Outputs 'True' if it is palindrome and 'False' if it isnt.
I/P:
Enter the string: abbabba
O.P:
Palindrome Check:  True
'''
'''
Function to check if palindrome using recursion
Parameters: string type 'string'
Return: Returns the bool True if it is palindrome and 'Fakse' if it isnt.
'''
def checkP(string):
    #Terminating condition when string gets empty
    if(len(string)==0):
        return True
    #Comparing first and last character
    if(string[0]!=string[-1]):
        return False
    #Returning the function call with no first and last element
    return checkP(string[1:len(string)-1])
'''
Main function for processing the logic of the program
Calling the required functions
And taking inputs from the user
Parameters: None
Return: Nothing, but prints bool for the required logic.
''' 
def main():
    #Inputting the string
    string=input("Enter the string: ")
    #If string is empty
    if(len(string)==0):
        print("String is empty.")
    else:
        #Stripping the extra spaces on both ends
        string=string.strip()
        #Printing the output
        print("Palindrome Check: ",checkP(string))
        
#Making main() as driver function
if __name__ == "__main__":
    main()