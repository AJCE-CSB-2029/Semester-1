def armstrong(num):
    length = len(str(num))
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** length
        temp //= 10
    return total

n = int(input("Enter a number: "))
arm = armstrong(n)

if n == arm:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
