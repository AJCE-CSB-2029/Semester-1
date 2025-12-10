file1 = open('python.txt', 'r')
content = file1.read()
file1.close()

file2 = open('python_1.txt', 'w')
file2.write(content)
file2.close()

file2 = open('python_1.txt', 'r')
copied_content = file2.read()
file2.close()

print("File copied successfully.\n", copied_content)
