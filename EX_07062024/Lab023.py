# List - Shopping List
# milk, bread, butter, poha
# 1. Add Item
# 2. Remove Item
# 3. Update Item
# 4. View Item
# 5. Exit
# List is mutable sequence

shopping_list = ["milk", "bread", "butter", "poha"]
print(shopping_list)
print(len(shopping_list))  # number of items is the length of the list
print(type(shopping_list))
print(shopping_list[0])  # milk
print(shopping_list[1])  # bread
print(shopping_list[-1])  # poha

# Append function to add item in the end
shopping_list.append("chocolate")  # add item to the list
print(shopping_list)

# Insert function to add item at a particaulr place
shopping_list.insert(1, "jam")  # add item in the middle of the list
# 1 matlab 1 number pe insert karna hai. Jam matlab 1 number pe jaam ko dalna hai.
print(shopping_list)

# extend function to add multiple items in the list
shopping_list.extend(["chips", "cookies"])
print(shopping_list)

#remove function to remove item from the list
shopping_list.remove("cookies")
print(shopping_list)

# pop function to remove item from the list
shopping_list.pop(2)  # 2 matlab 2 number pe remove karna hai. isne kaise remove kiya? >> 0 , 1, 2 aur 2 2 pe bread thi.
print(shopping_list)

print(shopping_list.index("butter"))  # index function to find the index of the item in the list
print(shopping_list.count("chips"))  # count function to find the number of times the item is repeated in the list

shopping_list.sort()  # sort function to sort the list in ascending order
print(shopping_list)
shopping_list.reverse()  # reverse function to reverse the list
print(shopping_list)

my_list = [1, 2, 3, 4, True, 3.14, "Aayushi"]
print(type(my_list))
