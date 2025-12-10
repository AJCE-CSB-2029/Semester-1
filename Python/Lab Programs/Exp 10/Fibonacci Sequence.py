n = int(input("Enter a number = "))

a = 0
b = 1
i = 0

while i < n:
    print(a)

    temp = a      # store old 'a'
    a = b         # update 'a'
    b = temp + b  # update 'b' using old 'a'

    i = i + 1