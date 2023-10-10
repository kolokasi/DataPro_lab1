# Define a function to read ciphertext data from a file
def read_ciphertext_data(file_path):
    ciphertext_data = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                encrypted_value = int(parts[1], 16)
                ciphertext_data.append(encrypted_value)
    return ciphertext_data

# Define a function to guess a key byte based on Fact 3
def guess_key_byte(iv_byte, d, known_key):
    key_byte_guess = (iv_byte + d + known_key) % 256
    return key_byte_guess

# Initialize the known part of the key (k0 + k1)
known_key = 0x7a

# Initialize the key bytes for k[0] to k[12]
key_bytes = [0] * 13

# Initialize variables to keep track of the previous key byte and IV
prev_key_byte = None
prev_iv_value = None

# Iterate through iv values from 5 to 14
for iv_value in range(5, 15):
    # Read ciphertext data from the corresponding file
    file_path = f"results_z_{iv_value}.txt"
    ciphertext_data = read_ciphertext_data(file_path)
    
    # Get the corresponding d[i] value
    d = sum(range(1, iv_value + 4))
    
    # Iterate through the ciphertext data and update the key based on Fact 3
    for ciphertext in ciphertext_data:
        iv_byte = iv_value - 3  # Calculate the iv_byte
        key_byte_guess = guess_key_byte(iv_byte, d, known_key)
        
        # Check if the key byte has changed
        if key_byte_guess != prev_key_byte or iv_value != prev_iv_value:
            print(f"Guess for k[{iv_value:02x}ffx]: {hex(key_byte_guess)}")
            prev_key_byte = key_byte_guess
            prev_iv_value = iv_value

