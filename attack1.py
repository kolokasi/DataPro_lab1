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
    print(ciphertext)
# Brute force m0 (single-byte plaintext)
for m0_guess in range(256):
    # Iterate through IV-ciphertext pairs
    successful_decryptions = 0
    
    for iv_hex, ciphertext in iv_ciphertext_pairs:
        iv = bytes.fromhex(iv_hex)
        key_guess = iv + bytes([m0_guess]) + os.urandom(12)  # Generate the key for each IV
        decrypted = rc4(key_guess, bytes([ciphertext]))
        
        if decrypted[0] == m0_guess:
            successful_decryptions += 1
        else:
            break  # Break if any decryption fails

    # If all ciphertexts were successfully decrypted with the guessed m0, print it
    if successful_decryptions == len(iv_ciphertext_pairs):
        print(f"Successful m0 guess: {m0_guess}")

# If no successful guess is found, indicate failure
print("Brute-force attack failed.")
                                       