'''
This program take a string input 'strn' to print the longest word/words
e.g:
I/P:Enter String to print largest Word:-Bhagesh plays guitar
O/P:Bhagesh
'''
def main():
    strn=input("Enter String to print largest Word:-")  
    strn=strn.strip()#Stripping the extra spaces from the both ends, as they will produce error in the program
    largestWord(strn)

'''
Function to print largest length words in the string
Purpose: printing longest word/words
Parameter: Inputted string 'strn'
Return: Nothing, but prints the longest word/words
'''
def largestWord(strn):
    words=strn.split(' ')#Making list spliting at space
    maxLen=0#Maxlength of largest word
    #Finding Maxlen 
    for word in words:
        if len(word)>maxLen:
            maxLen=len(word)
    #Printing max len words
    for word in words:
        if len(word)==maxLen:
            print(word)

#Making main() as driver function
if __name__ == "__main__":
    main()