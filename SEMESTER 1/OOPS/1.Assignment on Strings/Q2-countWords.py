'''
This program take a string input 's' to print number of words in the string.
e.g:
I/P:Enter string to find number of words: bhagesh dhankher is a mca student
O/P:6
'''

#Main Function: Driver function
def main():

    s=input("Enter string to find number of words: ")
    #Stripping extra white spaces from both the ends as they may produce errors
    s=s.strip()
    countWords(s)

'''
Function to count number of words.
Purpose: Counting words
Parameter: Inputted string 's'
Return: Nothing, but print the word count
'''

def countWords(s):
    wcount=1 #word counter
    #If empty string
    if(s==""):
        print("Empty String")
    #if string is non empty
    else:
        #Words counter is increased on every white space discovered
        for chr in s:
            if(chr==" "):
                wcount+=1
        print(wcount)
        
#Making main() as driver function
if __name__ == "__main__":
    main()