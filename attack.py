# Read the ciphertext data from the file
ciphertext_data = []

with open("res_01FFx.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            encrypted_value = int(parts[1], 16)
            ciphertext_data.append(encrypted_value)

# Calculate the XOR values for c[0] XOR (x+2)
xor_values = [(ciphertext ^ (x + 2)) % 256 for x, ciphertext in enumerate(ciphertext_data)]

# Find the most frequent value in the XOR values
most_frequent_value = max(set(xor_values), key=xor_values.count)

# The most frequent value is the guess for m[0]
m0_guess = most_frequent_value

print("Guess for m[0]:", hex(m0_guess))

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
m0= m0_guess
# Calculate the XOR values for (c[0] XOR m[0]) - x - 6 for iv=03 FF x
xor_values_03FF = [((ciphertext ^ m0 ) - x - 6) % 256 for x, ciphertext in enumerate(ciphertext_data_03FF)]

# Find the most frequent value in the XOR values for k[0] (iv=03 FF x)
k0_guess_03FF = max(set(xor_values_03FF), key=xor_values_03FF.count)

# Calculate the XOR values for (c[0] XOR m[0]) - x - 10 - k[0] - k[1] for iv=04 FF x
xor_values_04FF = [((ciphertext ^ m0) -x  - 10 - k0_guess_03FF) % 256 for x, ciphertext in enumerate(ciphertext_data_04FF)]

# Find the most frequent value in the XOR values for (k[0] + k[1]) (iv=04 FF x)
k0_k1_guess_04FF = max(set(xor_values_04FF), key=xor_values_04FF.count)

print("Guess for k[0]:", hex(k0_guess_03FF))
print("Guess for k[1]:", hex(k0_k1_guess_04FF))

def calculate_di_sum(count):
    di = sum(range(1, count + 4))
    return di


def find_k(filename, m0, count, previous_k):
    with open(filename, "r") as file:
        ciphertext_data = [int(line.strip().split()[1], 16) for line in file]
    di_sum = calculate_di_sum(count)
    xor_values = [((ciphertext ^ m0) - x - previous_k - di_sum) % 256 for x, ciphertext in enumerate(ciphertext_data)]
    k_guess = max(set(xor_values), key=xor_values.count)
    previous_k += k_guess
    return k_guess

# Example usage for each file
filenames = ["results_z_5.txt", "results_z_6.txt", "results_z_7.txt", "results_z_8.txt", "results_z_9.txt", "results_z_10.txt", "results_z_11.txt", "results_z_12.txt", "results_z_13.txt", "results_z_14.txt","results_z_15.txt"]
count = 2
previous_k = k0_guess_03FF + k0_k1_guess_04FF 
for filename in filenames:  
      # Initialize with the known key values
    k_values = find_k(filename, m0, count, previous_k)
    print(f"Guess for k[{count}]: {hex(k_values)}")
    previous_k += k_values
    count +=1

