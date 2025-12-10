#Method 1: Read Entire File at Once & Count Words (Less Efficient)

file = open('python.txt' , 'r')
content = file.read()
file.close()

print(content)

count = 0

for word in content.split():
    count = count + 1

print("Number of words in the file:", count)

#Method 2: Read File Line by Line & Count Words (More Efficient)

file = open('python.txt', 'r')
count = 0
for line in file:
    words = line.split()
    count += len(words)

print("Number of words in the file:", count)
file.close()
