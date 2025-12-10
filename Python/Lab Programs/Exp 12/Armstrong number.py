#Hint: 153 is an Armstrong number since 1^3 + 5^3 + 3^3 = 153

num = int(input("Input a number = "))  
temp = num
sum = 0

length = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

if num == sum:
    print("It is armstrong")
else:
    print("It's not armstrong")
