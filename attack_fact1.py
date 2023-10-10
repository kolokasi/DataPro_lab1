# Read the ciphertext data from the file
ciphertext_data = []

with open("res_01FFx.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            encrypted_value = int(parts[1], 16)
            ciphertext_data.append(encrypted_value)

# Calculate the XOR values for c[0] XOR (x+2)
xor_values = [(ciphertext ^ (x + 2)) for x, ciphertext in enumerate(ciphertext_data)]

# Find the most frequent value in the XOR values
most_frequent_value = max(set(xor_values), key=xor_values.count)

# The most frequent value is the guess for m[0]
m0_guess = most_frequent_value

print("Guess for m[0]:", hex(m0_guess))
