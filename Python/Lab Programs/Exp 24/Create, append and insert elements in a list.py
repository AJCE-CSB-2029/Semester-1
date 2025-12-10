n = int(input("Enter the number of elements : "))
my_list = [0] * n

for i in range(n):
    my_list[i] = int(input("Enter the elements : "))

print("List: ", my_list)

append_num = int(input("Enter an element to append: "))
my_list.append(append_num)
print("After appending: ", my_list)

insert_num = int(input("Enter a number to insert: "))
index = int(input("Enter the index to insert at: "))
my_list.insert(index, insert_num)
print("After insertion: ", my_list)