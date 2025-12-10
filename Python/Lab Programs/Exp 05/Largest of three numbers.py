a = int(input("Enter first number, a = "))
b = int(input("Enter second number, b = "))
c = int(input("Enter third number, c = "))

if a > b and a > c:
    print(a, "is the greatest.")
elif b > c:
    print(b, "is the greatest.")
else:
    print(c, "is the greatest.")
