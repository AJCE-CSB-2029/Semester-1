#Using built-in functions to find largest and smallest number in a list

numbers = eval(input("Enter the numbers as list: "))

largest = max(numbers)
smallest = min(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)

#Without using built-in functions to find largest and smallest number in a list

numbers = eval(input("Enter the numbers as list: "))

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)
