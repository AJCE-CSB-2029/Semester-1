list_0 = eval(input("Enter a list: "))

unique_list = []

for num in list_0:
    if num not in unique_list:
        unique_list.append(num)

unique_list.sort(reverse=True)

if len(unique_list) < 3:
    print("Not enough elements")
else:
    third_largest = unique_list[2]
    print("Third largest element:", third_largest)