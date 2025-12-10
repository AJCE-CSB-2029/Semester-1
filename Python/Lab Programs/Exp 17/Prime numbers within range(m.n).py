def is_prime(number):
    if number <= 1:
        return False
    for factor in range(2, int(number ** 0.5) + 1):
        if number % factor == 0:
            return False
    return True

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers between", start, "and", end, "are:")
for value in range(start, end + 1):
    if is_prime(value):
        print(value)