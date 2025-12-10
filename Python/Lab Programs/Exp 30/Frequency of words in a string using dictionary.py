string = input("Enter string: ")

words = string.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print("Word Frequency:", freq)