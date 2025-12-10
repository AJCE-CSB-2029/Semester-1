file = open('python.txt', 'w')
content_of_file = file.write("Hello world \nThis is a python program")
file.close()

file = open('python.txt', 'r')
content_of_file = file.read()
file.close()

print(content_of_file)