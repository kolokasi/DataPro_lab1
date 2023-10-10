# Read the ciphertext data from the file for iv=03 FF x (results_03FF.txt)
ciphertext_data_03FF = []

with open("results_03FF.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            encrypted_value = int(parts[1], 16)
            ciphertext_data_03FF.append(encrypted_value)

# Read the ciphertext data from the file for iv=04 FF x (results_04FF.txt)
ciphertext_data_04FF = []

with open("results_04FF.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            encrypted_value = int(parts[1], 16)
            ciphertext_data_04FF.append(encrypted_value)
m0=0xda
# Calculate the XOR values for (c[0] XOR m[0]) - x - 6 for iv=03 FF x
xor_values_03FF = [((ciphertext ^ m0 ) - x - 6) for x, ciphertext in enumerate(ciphertext_data_03FF)]

# Find the most frequent value in the XOR values for k[0] (iv=03 FF x)
k0_guess_03FF = max(set(xor_values_03FF), key=xor_values_03FF.count)

# Calculate the XOR values for (c[0] XOR m[0]) - x - 10 - k[0] - k[1] for iv=04 FF x
xor_values_04FF = [((ciphertext ^ m0) -x  - 10 - k0_guess_03FF) for x, ciphertext in enumerate(ciphertext_data_04FF)]

# Find the most frequent value in the XOR values for (k[0] + k[1]) (iv=04 FF x)
k0_k1_guess_04FF = max(set(xor_values_04FF), key=xor_values_04FF.count)

print("Guess for k[0] (iv=03 FF x):", hex(k0_guess_03FF))
print("Guess for (k[0] + k[1]) (iv=04 FF x):", hex(k0_k1_guess_04FF))
