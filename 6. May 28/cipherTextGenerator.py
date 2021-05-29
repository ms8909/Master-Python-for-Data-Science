# ARHAM RUMI

# Program to Cyber Security: substitution cipher

# Problem Statement

# --------------------------------------------------------------------------------------
# Write a function that 

# takes a message “m” and numeric offset “o”
# encrypts the messages by shifting all the letters in “m” by the offset “o”. 

# For example: With an offset of 3, “Hi” becomes “Kl” and so on. [Hint: use ord() and chr() python functions]
# --------------------------------------------------------------------------------------

print("Ciphering The Message")
print("\r")


def cipher(message, offset):

    print("\r")
    cipherMessage = ""
    cipher_char_ascii_val = 0
    for ch in message:
        char_ascii_val = ord(ch)
        cipher_char_ascii_val = char_ascii_val + offset
        cipher_char = chr(cipher_char_ascii_val)
        cipherMessage += cipher_char
    
    return cipherMessage


message = input("Enter Your Message : ")
offset = int(input("Enter the Offset : "))

cipherText = cipher(message, offset)
print("\r")

print(f"Your Plain Message is : {message}")
print(f"Your Ciphered Message is : {cipherText}")