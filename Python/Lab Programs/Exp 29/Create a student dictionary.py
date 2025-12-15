student = {}

n = int(input("How many items do you want to add?: "))

for i in range(n):
    key = input("Enter key: ")
    value = input(f"Enter the value for {key}: ")
    student[key] = value

print("Student Dictionary:", student)

# Accessing items
key_input = input("Enter a key to access: ")

if key_input in student:
    print(key_input, ":", student[key_input])
else:
    print("Invalid Key!")

# Accessing using get()
get_key = input("Enter a key to access using get(): ")

if get_key in student:
    print(get_key, ":", student.get(get_key))
else:
    print("Invalid Key!")

# Changing values
change_key = input("Enter the key to be changed: ")
change_value = input("Enter the new value: ")

if change_key in student:
    student[change_key] = change_value
    print("Value updated successfully")
else:
    print("Invalid Key!")

print("Updated student dictionary:", student)
