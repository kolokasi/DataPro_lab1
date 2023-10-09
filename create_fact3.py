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
    
    # Define the range of z values based on the requirement
    z_values = range(5, 15)
    
    for z in z_values:
        # Create a result file for each IV
        with open(f"results_z_{z}.txt", "w") as result_file:
            for x in range(256):
                # Calculate the corresponding i value for the current z
                i = z - 3
                
                d_i = calculate_di(i)
                
                # Calculate the value to be encrypted for iv=z FF x and ensure it's within the valid byte range
                value_z_FF_x = (x + d_i + sum(long_term_key[:i+1])) % 256
                
                # Construct the IV based on the description
                iv = bytes([z]) + b'\xFF' + bytes([x])
                
                # Encrypt plaintext with IV + long-term key for iv=z FF x
                encrypted_data = rc4(iv + long_term_key, bytes([value_z_FF_x]))
                
                # Write the IV and corresponding encrypted value to the result file
                result_file.write(f"0X{iv.hex().upper()} 0X{encrypted_data.hex().upper()}\n")

if __name__ == "__main__":
    main()