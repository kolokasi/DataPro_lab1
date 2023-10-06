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

def calculate_d(i):
    return sum(range(1, i + 4))

def calculate_key_offset(iv_byte):
    return iv_byte - 3

def main():
    # Long-term key (13 bytes)
    long_term_key = os.urandom(13)
    
    # Single-byte plaintext
    m = b'\x01'
    
    with open('files/res.txt', 'w') as file:
        # Write the actual key values to compare.txt
        with open('files/compare.txt', 'w') as compare_file:
            compare_file.write('Actual Key Values:\n')
            for i, k in enumerate(long_term_key):
                compare_file.write(f'Key {i}: {k}\n')
            compare_file.write(f'm0: {m[0]}\n')

        # Iterate through iv values as per the facts
        for iv_byte in range(256):
            iv = bytes([0x01, 0xFF, iv_byte])
            k0_offset = calculate_key_offset(iv_byte)
            d_i = calculate_d(k0_offset)
            
            # Calculate the first keystream byte based on the facts
            x = (iv_byte + 2 - k0_offset - d_i + sum(long_term_key[:k0_offset + 1])) % 256
            
            # Encrypt plaintext using RC4 with the derived key
            ciphertext = rc4(iv + long_term_key, m)
            
            # Write results to the file
            file.write(f'0X01FF{iv_byte:02X} 0X{ciphertext[0]:02X}\n')

if __name__ == "__main__":
    main()
