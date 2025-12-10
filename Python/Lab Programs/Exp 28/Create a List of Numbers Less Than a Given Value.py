master_list = eval(input("Enter the list of integers: "))
limit = int(input("Enter the limit number: "))

new_list = []

for num in master_list:
    if num < limit:
        new_list.append(num)

print("New list with numbers less than", limit, ":", new_list)