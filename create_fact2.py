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

    # ... (RC4 encryption code as provided)

def calculate_di(i):
    return sum(range(1, i + 4))

def main():
    # Long-term key (13 bytes)
    long_term_key = os.urandom(13)
    
    # Create result files to store IVs and encrypted values
    with open("results_03FF.txt", "w") as result_file_03FF, open("results_04FF.txt", "w") as result_file_04FF:
        for x in range(256):
            # Construct the IV for iv=03 FF x
            iv_03FF = bytes([0x03, 0xFF, x])
            
            # Calculate the value to be encrypted for iv=03 FF x and ensure it's within the valid byte range
            value_03FF = (x + 6 + long_term_key[0]) % 256
            
            # Encrypt plaintext with IV + long-term key for iv=03 FF x
            encrypted_data_03FF = rc4(iv_03FF + long_term_key, bytes([value_03FF]))
            
            # Write the IV and corresponding encrypted value to the results file for iv=03 FF x
            result_file_03FF.write(f"0X{iv_03FF.hex().upper()} 0X{encrypted_data_03FF.hex().upper()}\n")
            
            # Construct the IV for iv=04 FF x
            iv_04FF = bytes([0x04, 0xFF, x])
            
            # Calculate the value to be encrypted for iv=04 FF x and ensure it's within the valid byte range
            value_04FF = (x + 10 + long_term_key[0] + long_term_key[1]) % 256
            
            # Encrypt plaintext with IV + long-term key for iv=04 FF x
            encrypted_data_04FF = rc4(iv_04FF + long_term_key, bytes([value_04FF]))
            
            # Write the IV and corresponding encrypted value to the results file for iv=04 FF x
            result_file_04FF.write(f"0X{iv_04FF.hex().upper()} 0X{encrypted_data_04FF.hex().upper()}\n")

if __name__ == "__main__":
    main()