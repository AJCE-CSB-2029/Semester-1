# Using built-in function
s = input("Enter a string: ")

rev = "".join(reversed(s))

print("Reversed using built-in function:", rev)

# Using user-defined function
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

print("Reversed using function:", reverse_string(s))
