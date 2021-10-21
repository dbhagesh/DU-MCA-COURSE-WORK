""" The following code uses Additive Cipher technique to encrypt and then decrypt the given message(English alphabets).
    It uses additive key.
SAMPLE INPUT:   Enter the plain text: My Name is Shradha
                Enter the additive number to shift: 5
                Plain Text: My Name is Shradha
                Ciphered Text: Rd Sfrj nx Xmwfimf
                Deciphered Text: My Name is Shradha
"""


""" This function is to encrypt the given text.
parameter: plain_text, additive key.
returns: encrypted_text
"""


def additive_encrypt(plain_text, shift):

    encrypted_text = ""
    for character in plain_text[:]:
        #  for lower case letters only
        if(character.islower()):
            encrypted_text += chr((ord(character) + shift - 97) % 26 + 97)
        #  for upper case letters only
        elif(character.isupper()):
            encrypted_text += chr((ord(character) + shift - 65) % 26 + 65)
        #  for all the cases other than english alphabets
        else:
            encrypted_text += character

    # returns the appended final encrypted text
    return encrypted_text


""" This function is to decrypt the given text.
parameter: encrypted_text
returns: decrypted_text
"""


def additive_decrypt():

    decrypted_text = ""
    for character in encrypted_text[:]:
        if(character.islower()):
            #  for lower case letters only
            decrypted_text += chr((ord(character) - shift - 97) % 26 + 97)
        elif(character.isupper()):
            #  for upper case letters only
            decrypted_text += chr((ord(character) - shift - 65) % 26 + 65)
        else:
            #  for all the cases other than english alphabets
            decrypted_text += character
    # returns the appended final decrypted text
    return decrypted_text


# driver function
if __name__ == '__main__':

    # user input
    plain_text = input("Enter the plain text: ")
    shift = int(input("Enter the additive number to shift: "))
    print(f"Plain Text: {plain_text}")

    # calling encrypt and decrypt functions
    encrypted_text = additive_encrypt(plain_text, shift)
    print(f"Ciphered Text: {encrypted_text}")
    print(f"Deciphered Text: {additive_decrypt()} \n")
