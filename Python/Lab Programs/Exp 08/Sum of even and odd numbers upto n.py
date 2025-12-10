n = int(input("Enter the value of n = "))

even_sum = 0
odd_sum = 0
i = 1

while i <= n:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
    i = i + 1

print("Sum of even natural numbers up to", n, "=", even_sum)
print("Sum of odd  natural numbers up to", n, "=", odd_sum)
