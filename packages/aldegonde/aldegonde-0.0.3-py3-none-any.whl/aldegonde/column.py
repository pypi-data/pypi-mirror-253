"""
docstring
"""


def encrypt_message(message: str, key: str, padding: str = " ") -> str:
    """
    columnar transposition
    """
    message = message.replace(" ", "").upper()
    num_cols = len(key)
    num_rows = -(-len(message) // num_cols)  # Ceiling division
    message += padding * (num_rows * num_cols - len(message))

    # Create an empty matrix to store the message
    matrix: list[list[str]] = [["" for _ in range(num_cols)] for _ in range(num_rows)]

    # Fill the matrix column by column
    index = 0
    for row in range(num_cols):
        for col in range(num_rows):
            matrix[row][col] = message[index]
            index += 1

    # Read the matrix column by column to get the encrypted message
    ciphertext = ""
    for col in range(1, num_cols + 1):
        col_index = key.index(str(col))
        print(col_index)
        for row in range(num_rows):
            ciphertext += matrix[row][col_index]

    return ciphertext


def decrypt_message(ciphertext: str, key: str) -> str:
    """
    columnar transposition
    """
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols

    # Create an empty matrix to store the encrypted message
    matrix = [["" for _ in range(num_cols)] for _ in range(num_rows)]

    # Calculate the number of characters in the last row
    last_row_chars = len(ciphertext) % num_cols

    # Track the number of characters taken from the encrypted message
    taken_chars = 0

    # Fill the matrix column by column
    for col in range(num_cols):
        col_index = key.index(str(col + 1))
        extra_char = 1 if col_index < last_row_chars else 0

        for row in range(num_rows - extra_char):
            matrix[row][col_index] = ciphertext[taken_chars]
            taken_chars += 1

    # Read the matrix row by row to get the decrypted message
    plaintext = ""
    for row in range(num_rows):
        for col in range(num_cols):
            plaintext += matrix[row][col]

    return plaintext


if __name__ == "__main__":
    plaintext = """The nose is pointing down and the houses are getting bigger"""
    key = "1423756"
    encrypted = encrypt_message(plaintext, key)
    print("ciphertext:", encrypted)

    decrypted = decrypt_message(encrypted, key)
    print("Decrypted:", decrypted)
