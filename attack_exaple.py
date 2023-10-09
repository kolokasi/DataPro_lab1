from collections import Counter

# Read ciphertexts from the "res.txt" file
with open("files/res.txt", "r") as file:
    lines = file.readlines()
    ciphertexts = [int(line.split()[1], 16) for line in lines]


# Compute the XOR values and count their frequencies
results = [ciphertexts[0] ^ (x + 2) for x in range(256)]
counter = Counter(results)

# Find the most frequent result
most_frequent_result = counter.most_common(1)[0][0]

# The most frequent result is our guess for m[0]
guess_m0 = most_frequent_result
print(f"Guess for m[0]: {guess_m0}")