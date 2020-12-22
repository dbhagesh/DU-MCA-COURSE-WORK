'''
This program take a string input 'strn' to print reverse of each word in the string
e.g:
I/P:Enter string to rev its each word:-bhagesh dhankher is mca student
O/P:hsegahb rehknahd si acm tneduts
'''
#Main function: Driver function
def main():
    strn=input("Enter string to rev its each word:-")
    strn=strn.strip() #Stripping the extra spaces from the both ends, as they will produce error in the program
    revEachWord(strn)


'''
Function to reverse each word of a string
Purpose: reversing each word of string
Parameter: Inputted string 'strn'
Return: Nothing, but prints the reverse of each word in the string
'''
def revEachWord(strn):
    #A temp string to store individual word
    word=""
    #Reversing individual word and printing them
    for chr in strn:
        if(chr==" "):
            print(word[::-1],end=" ")
            word=""
        else:
            word+=chr
    #Printing the last word in the string
    print(word[::-1],end=" ")

#Making main() as driver function
if __name__ == "__main__":
    main()

