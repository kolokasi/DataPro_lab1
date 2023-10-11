from collections import Counter
# Read the ciphertext data from the file for iv=03 FF x (results_03FF.txt)
ciphertext_data_05FF = []

with open("results_z_5.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            encrypted_value = int(parts[1], 16)
            ciphertext_data_05FF.append(encrypted_value)

m0=0xda
k0 = 0x04
k1 = 0x5c

# Calculate the XOR values and reduce them modulo 256
xor_values_05FF = [((ciphertext ^ m0) - x - k0 - k1 - 15) % 256 for x, ciphertext in enumerate(ciphertext_data_05FF)]

# Find the most frequent value in the XOR values for k[2] (iv=05 FF x)
k0_guess_05FF = max(set(xor_values_05FF), key=xor_values_05FF.count)


#print([hex(val) for val in xor_values_03FF])
print(k0_guess_05FF )
value_counts = Counter(xor_values_05FF)
count = xor_values_05FF.count(207)
print(f"'c6' appears {count} times.")