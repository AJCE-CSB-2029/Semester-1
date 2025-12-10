list_1 = eval(input("Enter List 1: "))
list_2 = eval(input("Enter List 2: "))

max_len = max(len(list_1), len(list_2))

result = []

for i in range(max_len):
    a = list_1[i] if i < len(list_1) else 0
    b = list_2[i] if i < len(list_2) else 0
    result.append(a + b)

print("Resultant List:", result)