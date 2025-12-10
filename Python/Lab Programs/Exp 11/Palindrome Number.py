#Hint: 121 is a Palindrome number since 121 reversed is still 121

n = int(input("Input a number = "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("It is a Palindrome")
else:
    print("It's not a Palindrome")
