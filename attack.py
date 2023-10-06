import os

# RC4 implementation for both encryption and decryption
def rc4(key, data):
    S = list(range(256))
    j = 0
    key = bytearray(key)
    data = bytearray(data)
    
    # Key-scheduling algorithm
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    j = 0
    output = bytearray()
    
    # Pseudo-random generation algorithm
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        output_byte = char ^ k
        output.append(output_byte)
    
    return bytes(output)

# Read the data from res.txt
with open('files/res.txt', 'r') as file:
    lines = file.readlines()

# Initialize a list to store IV-ciphertext pairs
iv_ciphertext_pairs = []

# Extract IVs and ciphertexts from the file
for line in lines:
    parts = line.split()
    iv_hex = parts[0][2:]  # Remove the "0X" prefix and use the rest of the string as IV
    ciphertext = int(parts[1], 16)
    iv_ciphertext_pairs.append((iv_hex, ciphertext))

# Initialize an empty key
key_guess = bytes([0] * 13)

# Brute force all 13 bytes of the key
for byte_index in range(13):
    for key_byte_guess in range(256):
        key_guess = key_guess[:byte_index] + bytes([key_byte_guess]) + key_guess[byte_index + 1:]
        
        # Check if this key successfully decrypts all ciphertexts
        successful_decryptions = 0
        for iv_hex, ciphertext in iv_ciphertext_pairs:
            iv = bytes.fromhex(iv_hex)
            decrypted = rc4(iv + key_guess, bytes([ciphertext]))
            if decrypted[0] == key_byte_guess:
                successful_decryptions += 1
            else:
                break  # Break if any decryption fails
        
        # If all ciphertexts were successfully decrypted with this byte of the key, update the key guess
        if successful_decryptions == len(iv_ciphertext_pairs):
            print(f"Successful byte {byte_index} guess: {key_byte_guess}")
        else:
            # If any decryption fails, reset the key_guess for the next attempt
            key_guess = bytes([0] * 13)

# Print the final key
print(f"Brute-force attack completed. Key: {key_guess.hex().upper()}")
