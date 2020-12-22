'''
This program take a string input 's' to print its reverse
e.g:
I/P:Enter the string:-bhagesh
O/P:Vowels are: 2  Consonants are: 5  Special Characters are: 0
'''
def main():
    strn=input("Enter the string:-")
    #Converting all the string in lower case for checking less cases 
    strn=strn.lower()
    countf(strn)


'''
Function to count vowels,consonants and special characters
Purpose: Counting different type characters in the string
Parameter: Inputted string 'strn'
Return: Nothing, but print the vowel,consonants and special character count
'''

def countf(strn):
    v=0#vowel counter
    c=0#consonant counter
    s=0#special character counter
    
    for chr in strn:
        #Filtering vowels
        if(chr=='a'or chr=='e' or chr=='i' or chr=='o' or chr=='u'):
            v+=1
        #Filtering consonants
        elif(chr>='a' and chr<='z'):
            c+=1
        #Filtering special characters
        elif(not(chr>='0' and chr<='9')):
            s+=1
    print("Vowels are:",v," Consonants are:",c," Special Characters are:",s)

#Making main() as driver function
if __name__ == "__main__":
    main()