#Using a temporary variable

a = int(input("Input first number, a = "))
b = int(input("Input second number, b = "))

temp = a
a = b
b = temp

print("Swapped value of a = ", a)
print("Swapped value of b = ", b)
