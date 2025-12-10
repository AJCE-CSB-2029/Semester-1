n = int(input("Enter a number = "))

if n < 0:
    print("Factorial is not possible for a negative number.")
elif n == 0:
    print("Factorial = 1")
else:
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    print("Factorial of", n, "=", fact)
