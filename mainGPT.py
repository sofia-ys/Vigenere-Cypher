import os

def cipher(message, key, decrypt=False):
    ''' Encrypt or decrypt a message using the Vigenere cipher. '''
    newmsg = ''
    key = key.upper()
    key_index = 0
    key_length = len(key)

    for char in message:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            if decrypt:
                shift = -shift

            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            newmsg += new_char
            key_index += 1  # Only increment on alphabetic characters
        else:
            newmsg += char  # Keep non-letters unchanged

    return newmsg

# === MAIN EXECUTION FOR ALL MESSAGES ===

# Ensure 'processed/' directory exists
os.makedirs('processed', exist_ok=True)

# Read keys from keys.txt
with open('keys.txt', 'r') as f:
    keys = [line.strip() for line in f.readlines()]

# Loop through message0.txt to message4.txt
for i in range(5):
    message_path = f'data/message{i}.txt'
    output_path = f'processed/output{i}.txt'
    key = keys[i]

    # Read encrypted message
    with open(message_path, 'r', encoding="utf-8") as f:
        encrypted_message = f.read()

    # Decrypt
    decrypted_message = cipher(encrypted_message, key, decrypt=True)

    # Write output
    with open(output_path, 'w') as f:
        f.write(decrypted_message)

    print(f"Decrypted message{i}.txt using keyword '{key}'")
    print(f"Saved result to {output_path}")
