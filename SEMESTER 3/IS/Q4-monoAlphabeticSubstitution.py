from collections import defaultdict
import random

# Global Variable
frequencyAlphabets = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

'''
Purpose : Function to perform frequency attack Substitution Cipher.

Parameters :
    S : Containing the
    Type : Str

    N : Number of Decoded Strings
    Type : Int

Return Type : String
'''


def frequencyAttack(S, N):
    # Decoded Strings
    decodedStrings = []

    # Considering the frequency Aplbhatets as the key
    key = frequencyAlphabets

    for i in range(N):

        # key
        key = ''.join(random.sample(key, len(key)))
        key = key.upper()

        # Decoded String
        decoded = ""

        # Generating Decoded String
        for j in range(len(S)):
            # If space keep as it is
            if(S[j] == ' '):
                decoded += ' '
            # Else find the index of char in key and get the corresponding alphabet
            else:
                decoded += chr(key.index(S[j])+65)

        decodedStrings.append(decoded)

    return decodedStrings


'''
Purpose : Function called on program start
          Input Encoded String
Output : Decoded Texts
'''


def main():
    # Input
    S = input("Enter Cipher Text : ")
    S = S.upper()
    N = int(input("Specify Number of Results needed : "))

    # Performing FrequencyAttack
    decodedStrings = frequencyAttack(S, N)

    print("\n\nDECODING... \n")

    for i in decodedStrings:
        print("Decoded String : ", i)


if __name__ == '__main__':
    main()
