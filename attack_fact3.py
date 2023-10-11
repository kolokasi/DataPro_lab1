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
previous_k = 0x04 + 0x5C 
for filename in filenames:
    m0=0xda  
      # Initialize with the known key values
    k_values = find_k(filename, m0, count, previous_k)
    print(f"K values for {filename}: {hex(k_values)}")
    previous_k += k_values
    count +=1
