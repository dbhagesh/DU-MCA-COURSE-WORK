import math

""" The following code uses Affine Cipher technique to encrypt and then decrypt the given message(English alphabets).
    It uses two keys multiplicative and additive.
SAMPLE INPUT:   Enter the plain text: My Name is Shradha 
                Enter a (coprime to 26, not equal to 1): 5
                Enter b: 7
                encrypted text: Px Uhpb vt Tqohwqh
                decrypted text: My Name is Shradha
"""


""" This function is to encrypt the given text.
parameter: plain_text, multiplicative key, additive key.
returns: encrypted_text
"""
def affine_encrypt(plain_text, a, b):

    encrypted_text = ""
    for character in plain_text[:]:
        #  for upper case letters only
        if(character.isupper()):
            encrypted_text += chr((a * (ord(character) - 65) + b) % 26 + 65)
        #  for lower case letters only
        elif(character.islower()):
            encrypted_text += chr((a * (ord(character) - 97) + b) % 26 + 97)
        #  for all the cases other than english alphabets
        else:
            encrypted_text += character
    # returns the appended final encrypted text
    return encrypted_text

""" This function is to decrypt the given text.
parameter: encrypted_text, multiplicative key, additive key.
returns: decrypted_text
"""
def affine_decrypt(encrypted_text, a, b):
    
    decrypted_text = ""
    for character in encrypted_text[:]:
        #  for upper case letters only
        if(character.isupper()):
            decrypted_text += chr((affine_inverse(a) * (ord(character) - 65 - b)) % 26 + 65)
        #  for lower case letters only
        elif(character.islower()):
            decrypted_text += chr((affine_inverse(a) * (ord(character) - 97 - b)) % 26 + 97)
        #  for all the cases other than english alphabets
        else:
            decrypted_text += character
    # returns the appended final decrypted text
    return decrypted_text


"""This function is to find the inverse of the multiplicative key w.r.t mod 26.
parameter: multiplicative key, a.
returns: inverse of the key."""
def affine_inverse(a):

    for a_inverse in range(1, 26):
        # for range 1 to 26 it finds the inverse
        check = (a * a_inverse) % 26
        # we check if the above value is 1 then we have got the inverse
        if (check == 1):
            return a_inverse
    

if __name__ == '__main__':

    # user input
    plain_text = input("Enter the plain text: ")
    a = int(input("Enter a (coprime to 26, not equal to 1): "))

    # a should be coprime to 26
    if(math.gcd(a, 26) != 1):
        raise Exception("Wrong value of 'a' Entered.")

    b = int(input("Enter b: "))

    # calling encrypt and decrypt functions
    encrypted_text = affine_encrypt(plain_text, a, b)
    print(f"encrypted text: {encrypted_text}")
    decrypted_text = affine_decrypt(encrypted_text, a, b)
    print(f"decrypted text: {decrypted_text} \n")


