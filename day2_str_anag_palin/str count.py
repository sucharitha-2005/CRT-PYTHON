text = 'aaabbbcccc'
char_counts = {}

# Iterate and populate dictionary
for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1

print(char_counts)

