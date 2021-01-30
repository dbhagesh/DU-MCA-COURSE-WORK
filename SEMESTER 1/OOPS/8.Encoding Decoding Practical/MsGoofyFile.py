'''
--Included file operations in the MsGoofy program
It takes the message from the "message.txt" file: This file should have the message

It reads the message from the "message.txt" file and stores the encoded message into encodedstring.txt
And then reads the endoded message from encodedstring.txt and then stores the decoded message into 
decodedstring.txt
'''
'''
Today Ms. GOOFY has to send a message to her friend but in a secure manner. She designed her own way of encoding and decoding messaging. 
Foe encoding, she assumed the following:
Given any number, she returns the corresponding text in words but in reverse order.
If it is a character, then take its ASCII value and reversed it.
Also, inserted a space between each encoded o/p.
For any special character, take it as it is

e.g. if input is : A34$ is Terr60Sist
o/p: 56 eerht ruof $  501 511  48 101 411 411 xis orez 38 501 511 611

For decoding, the reverse of above is conducted.
i.e. input: 56 eerht ruof $  501 511  48 101 411 411 xis orez 38 501 511 611
output: A34$ is Terr60Sist

'''
import os.path
from os import path
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
        #Checking if the unit is ascii value of alphabets
        if(i.isnumeric())and(str(chr(int(revWord(i)))).isalpha()):
            dmsg+=chr(int(revWord(i)))
        #Checking if i is reversed number
        elif(revWord(i) in wordTonum):
            dmsg+=wordTonum[revWord(i)]
        #Space is stored as empty string in the msg after split
        #So checking for empty space
        elif(i==""):
            dmsg+=" "
        #Anything else is stored as it is
        else:
            dmsg+=i
    #Returning the decoded message
    return dmsg

'''
Function create message.txt file which contains the message to encode
Input: string-> 'name': name of the file, 'mode': mode of opening the file
Write: Writes the message in the file
'''
def message_file(name,mode):
    #Exception handling
    try:
        #Opening the file
        f=open(name,mode)
        #Reading the message to deal with from the file
        msg=f.read()
        #Encoded message
        print("Message is: ",msg)
        #closing the file
        f.close()
        return msg
    #if exception occurs
    except:
        print("Cant read from message file.")
'''        
Function to write into message file when message file isnt present.
Inputs: string-> 'name': name of the file, 'mode': mode of opening the file
Output: Creates the message.txt file and writes the message to the file.
'''
def write_message_file(name,mode):
    #Exception handling
    try:
        #Opening the file
        f=open(name,mode)
        #Reading the message to deal with from the file
        print("As message file doesnt exist.")
        print("Creating message file.")
        print("Please enter the message below-")
        msg=input()
        f.write(msg)
        #closing the file
        f.close()
    #if exception occurs
    except:
        print("Cant write to message file.")
'''
Function create encodedstring.txt file which contains the encoded message
Input: string-> 'name': name of the file, 'mode': mode of opening the file, 'msg': message to encode
Write: Writes the encoded message in the file
'''
def encode_file(name,mode,msg):
    #Exception handling
    try:
        #Opening the file
        f=open(name,mode)
        #Calling encode function for encoding the message
        emsg=encode(msg)
        #Encoded message
        print("Encoded message:")
        print(emsg)
        #Writing the encoded message
        f.write(emsg)
        #closing the file
        f.close()
    #if exception occurs
    except:
        print("Cant write the encoded file.")

'''
Function create decodedstring.txt file which contains the decoded message
Input: string-> 'name': name of the file, 'mode': mode of opening the file, 'msg': message to decode
Write: Writes the decoded message in the file
'''       
def decode_file(name,mode,msg):
    #Exception handling
    try:
        #Opening the file
        f=open(name,mode)
        #Calling the deoce message function
        dmsg=decode(msg)
        #Printing the decoded message
        print("Decoded message:")
        print(dmsg)
        #Writing the message in the file
        f.write(dmsg)
        #Closing the file
        f.close()
    #If errors occurs
    except:
        print("Cant write the decoded file.")   
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
            if(not(path.exists("message.txt"))):
                write_message_file("message.txt","wt")
            msg=message_file("message.txt","rt")
            print("----Encoding-----")
            print("----Encoding-----")
            print("----Encoding Done-----")
            #Calling encode_file function
            encode_file("encodedstring.txt","wt",msg)
            print("----Encoded Message stored in file successfully----")
            break

        if(inp==2):
            #Inputted msg
            f=open("encodedstring.txt","rt")
            msg=f.read()
            print("----Decoding-----")
            print("----Decoding-----")
            print("----Decoding Done-----")
            #Calling decode_file function
            decode_file("decodedstring.txt","wt",msg)
            print("----Decoded Message stored in file successfully----")
            break



#Making main() as the driver function  
if __name__ == "__main__":
    main()