def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not possible"
    else:
        return x / y

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Sum:", add(num1, num2))
elif choice == 2:
    print("Difference:", subtract(num1, num2))
elif choice == 3:
    print("Product:", multiply(num1, num2))
elif choice == 4:
    print("Division:", divide(num1, num2))
else:
    print("Invalid choice")
