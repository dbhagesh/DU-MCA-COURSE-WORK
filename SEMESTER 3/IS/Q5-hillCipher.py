""" The following code uses Hill Cipher technique to encrypt and then decrypt the given message(Uppercase english alphabets) using 2 x 2 matrix as key.
NOTE: In order to apply this technique the input message has to be of even length to facilitate matrix multiplication. 
      Given an odd length message the letter 'X' is appended to it.
      
SAMPLE INPUT:   Enter the message: MYNAMEISSHRADHA
                Enter the 4 length key for 2 X 2 matrix: HILL
                Encrypted Text:  UQTAEGEYSDSAJRKJ
                Decrypted Text:  MYNAMEISSHRADHAX """


"""This function is to find the inverse of the determinant w.r.t mod 26
parameter: determinant.
returns: inverse of the determinant"""


def det_inverse(input):
    # list of posssible inverses of determinant
    possible_inverses = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    if input not in possible_inverses:
        # throw an exception if inverse cannot be calculated.
        raise Exception(
            f"inverse for determinant {input} does not exist. There are only 12 possibilties for the determinant: 1,3,5,7,9,11,15,17,19,21,23,25.")

    # finding inverse
    for inverse in range(1, 27):
        check = (input * inverse) % 26
        if (check == 1):
            return inverse


"""This function is to find the inverse of the key matrix.
parameter: the key matrix.
returns: inverse of the key matrix."""


def get_matrix_inverse(m):

    # finding determinant
    determinant = (m[0][0]*m[1][1]-m[0][1]*m[1][0]) % 26

    # determinant should be between 0 - 26
    if(determinant < 0):
        determinant = 26 + determinant

    # finding determinant inverse.
    det_inv = det_inverse(determinant)

    # for 2x2 matrix the elements other than diagonal matrix becomes negative, so keep its value in between 0 - 26
    m[0][1] = 26 - m[0][1]
    m[1][0] = 26 - m[1][0]

    # inverse matrix
    return [[(m[1][1] * det_inv) % 26, (m[0][1] * det_inv) % 26],
            [(m[1][0] * det_inv) % 26, (m[0][0] * det_inv) % 26]]


"""This function is to encrypt and decrypt the message.
parameter: key matrix(encrypt)/inverse key matrix(decrypt), input_message as a matrix(encrypt)/encrypted_message as a matrix(decrypt).
returns: a encrypted/decrypted matrix."""


def hill_cipher(key_matrix, input_matrix):

    num_of_cols = len(input_matrix[0])

    # output_matrix to store the calculated result
    output_matrix = [[0] * num_of_cols for x in range(2)]

    # matrix multiplication
    for row in range(2):
        for col in range(num_of_cols):
            output_matrix[row][col] = 0
            for i in range(2):
                output_matrix[row][col] += (key_matrix[row]
                                            [i] * input_matrix[i][col])
            output_matrix[row][col] %= 26

    return output_matrix


"""This function is to convert a message into a matrix.
parameter: encrypted_matrix/decrypted_matrix.
returns: a encrypted/decrypted message."""


def matrix_to_message(input_matrix):

    # output_text to store the calculated result
    output_text = ""
    for row in range(2):
        for col in range(len(input_matrix[0])):
            # converting numbers to english alphabets and store it to output_text
            output_text += chr(input_matrix[row][col] + 65)
    return output_text


"""This function is to take the inputs of the user the message ans the key and feed them to hill_cipher to perform encryption/decryption.
parameter: plain_text, key.
returns: None"""


def main(plain_text, key):

    size = len(plain_text) // 2
    key_matrix = [[0] * 2 for x in range(2)]
    plain_text_matrix = [[0] * size for x in range(2)]

    # conerting user input key to 2 x 2 matrix form
    index = 0
    for row in range(2):
        for col in range(2):
            key_matrix[row][col] = ord(key[index]) % 65
            index += 1

    # conerting user input message to 2 x k(size) matrix form
    index1 = 0
    for row in range(2):
        for col in range(size):
            plain_text_matrix[row][col] = ord(plain_text[index1]) % 65
            index1 += 1

    # calling the function hill_cipher
    encrypted_matrix = hill_cipher(key_matrix, plain_text_matrix)
    print("Encrypted Text: ", matrix_to_message(encrypted_matrix))

    decrypted_matrix = hill_cipher(
        get_matrix_inverse(key_matrix), encrypted_matrix)
    print("Decrypted Text: ", matrix_to_message(decrypted_matrix))


# driver function
if __name__ == '__main__':

    # taking user input
    plain_text = input("Enter the message: ")
    # if length odd append 'X'
    if (len(plain_text) % 2) != 0:
        plain_text += "X"

    key = input("Enter the 4 length key for 2 X 2 matrix: ")

    # calling main function
    main(plain_text, key)
