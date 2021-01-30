'''
Today Ms. GOOFY has to send a message to her friend but in a secure manner. She designed her own way of encoding and decoding messaging. 
Foe encoding, she assumed the following:
Given any number, she returns the corresponding text in words but in reverse order.
If it is a character, then take its ASCII value and reversed it.
Also, inserted a space between each encoded o/p.
For any special character, take it as it is

e.g. if input is : 3AD$2a
o/p:  eerht 56  86 $ owt 79

For decoding, the reverse of above is conducted.
i.e. input: eerht 56  86 $ owt 79
output: 3AD$2a

'''

'''
Function to reverse the string
Input: A string type 'string'
Return: reverse of 'string'
'''
def revWord(string):
    return string[-1::-1]
'''
Function to encode the message
Input: Message to encode 'msg'
Return: Returns 'emsg' which is the encoded message
'''
def encode(msg):
    #Dictionary for reversing numbers
    numToWord={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}
    #Encoded message
    emsg=""
    #Traversing
    for i in msg:
        #If it is a number
        if(i>='0' and i<='9'):
            emsg+=revWord(numToWord[i])+" "
        #If it is an aplhabet
        elif (i>='a' and i<='z') or (i>='A' and i<='Z'):
            emsg+=revWord(str(ord(i)))+ " "
        #If special character or space
        elif (i==" "):
            emsg+=i
        else:
            emsg+=i+" "
    #Returning encoded message
    return emsg
'''
Function to decode the message
Input: Message to decode 'msg'
Return: Returns 'dmsg' which is the decoded message
'''

def decode(msg):
    #Dictionary to refer each word to number
    wordTonum={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
   
    #Decoded message
    dmsg=""
    #Spliting the message with spaces
    msg=msg.split(" ")
    #Traversing
    for i in msg:
    
        if(i.isnumeric())and(str(chr(int(revWord(i)))).isalpha()):
            dmsg+=chr(int(revWord(i)))
        elif(revWord(i) in wordTonum):
            dmsg+=wordTonum[revWord(i)]
        elif(i==""):
            dmsg+=" "

        else:
            dmsg+=i
    
    return dmsg

        

'''
Main function for processing the logic of the program
Calling the required functions
And taking inputs from the user
Parameters: None
Return: Nothing, but prints the encoded/decoded string.
'''       
def main():
    while(True):
        #Inputting 1 to encode 2 to decode
        inp=int(input("Enter '1': To encode message or '2': To decode a message: "))
        if(inp==1):
            #Inputted message
            msg=input("Enter the message: ")
            print("----Encoding-----")
            print("----Encoding-----")
            print("----Encoding Done-----")
            #Calling encoding function
            emsg=encode(msg)
            print(emsg)
            break

        if(inp==2):
            #Inputted msg
            msg=input("Enter the message: ")
            print("----Decoding-----")
            print("----Decoding-----")
            print("----Decoding Done-----")
            #Calling decoding function
            dmsg=decode(msg)
            print(dmsg)
            break



#Making main() as the driver function  
if __name__ == "__main__":
    main()