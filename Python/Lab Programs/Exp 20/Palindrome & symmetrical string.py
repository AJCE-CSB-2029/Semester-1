s = input("Enter a string: ")

# Check palindrome
if s == s[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")

# Check symmetrical
half = len(s) // 2

if len(s) % 2 == 0:
    first_half = s[:half]
    second_half = s[half:]
else:
    first_half = s[:half]
    second_half = s[half+1:]

if first_half == second_half:
    print("The string is Symmetrical")
else:
    print("The string is not Symmetrical")
