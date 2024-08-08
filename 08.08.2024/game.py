def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

message = "Hello, World!"
shift = 3
encrypted_message = encrypt(message, shift)
print(f"Encrypted: {encrypted_message}")
decrypted_message = decrypt(encrypted_message, shift)
print(f"Decrypted: {decrypted_message}")
