def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a given text using the Caesar Cipher algorithm.

    Parameters:
    text (str): The input text to be encrypted or decrypted.
    shift (int): The number of positions to shift each letter.
    mode (str): 'encrypt' to encrypt the text, 'decrypt' to decrypt it.

    Returns:
    str: The encrypted or decrypted text.
    """
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters are added unchanged
            result += char

    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    
    while True:
        # Get user input for the message and shift value
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
        
        # Get user choice for encryption or decryption
        choice = input("Do you want to (e)ncrypt or (d)ecrypt the message? (e/d): ").lower()
        
        if choice == 'e':
            encrypted_message = caesar_cipher(message, shift, mode='encrypt')
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = caesar_cipher(message, shift, mode='decrypt')
            print(f"Decrypted Message: {decrypted_message}")
        else:
            print("Invalid choice! Please enter 'e' for encrypt or 'd' for decrypt.")
        
        # Ask if the user wants to continue
        continue_choice = input("Do you want to continue? (y/n): ").lower()
        if continue_choice != 'y':
            print("Thank you for using the Caesar Cipher Program!")
            break

if __name__ == "__main__":
    main()