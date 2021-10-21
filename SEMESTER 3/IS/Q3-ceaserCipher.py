from collections import defaultdict

# Global Variable
frequencyAlphabets = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

'''
Purpose : Function to perform frequency attack Ceaser Cipher.

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

    # Creating Frequency Dictionary
    frequencyDict = defaultdict(int)
    for c in S:
        frequencyDict[c] += 1

    # Sorted by value
    sorted_frequency = list(
        sorted(frequencyDict.items(), key=lambda item: item[1]))

    for i in range(N):

        # Deciding Shift value
        shift = ((26 + ord(sorted_frequency[0][0]) -
                  ord(frequencyAlphabets[i])) % 26)
        decoded = ""

        # Generating Decoded String
        for j in range(len(S)):

            if(S[j] >= 'A' and S[j] <= 'Z'):
                decoded += chr(65 + (ord(S[j]) - 65 + shift) % 26)
            else:
                decoded += S[j]

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
    print("Note : At max there can be 26 results.")
    N = int(input("Specify Number of Results needed : "))

    # Performing FrequencyAttack
    decodedStrings = frequencyAttack(S, N % 26)

    print("\n\nDECODING... \n")

    for i in decodedStrings:
        print("Decoded String : ", i)


if __name__ == '__main__':
    main()
