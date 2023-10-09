import os

def rc4(key, plaintext):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    i = j = 0
    ciphertext = []
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        ciphertext_byte = char ^ k
        ciphertext.append(ciphertext_byte)
    
    return bytes(ciphertext)

def calculate_di(i):
    return sum(range(1, i + 4))

def main():
    # Long-term key (13 bytes)
    long_term_key = os.urandom(13)
    
    # Create a result file to store IVs and encrypted values
    with open("res_01FFx.txt", "w") as result_file:
        for x in range(256):
            # Construct the IV based on the description
            iv = bytes([0x01, 0xFF, x])
            
            # Encrypt plaintext with IV + long-term key
            encrypted_data = rc4(iv + long_term_key, bytes([(x + 2) % 256]))
            
            # Write the IV and corresponding encrypted value to the results file
            result_file.write(f"0X{iv.hex().upper()} 0X{encrypted_data.hex().upper()}\n")

if __name__ == "__main__":
    main()
