# List
# List -Collection of items (Duplicate is allowed)

my_list = [1, 2, 3, 4]
# my_list = [1, "Hello", 3.4, True]  # mixed data types

# Indexing
print("Element at index 0: ",  my_list[0])

# chamging an element
my_list[1] = 20
print("List after changing the element at index 1: ", my_list)

# append - will add in the end

my_list.append(123)
print("List after appending an element: ", my_list)

#extend - will add multiple elements in the list

my_list.extend([78, 45, 69])
print("List after extending: ", my_list)

# insert - will add an element at a specific index

my_list.insert(1, 'a')
print("List after inserting an element: ", my_list)

# remove - will remove an element from the list

my_list.remove('a')
print("List after removing an element: ", my_list)

# copy  - will create a copy of the list

new_list = my_list.copy()
print("New list: ", new_list)

#  clear - will clear all the elements from the list

my_list.clear()
print("List after clearing: ", my_list)
print("copy: ", new_list)   # copy of the list remains

# print index

#print("Index of 3 in the list : ",  new_list.index(3))

# Sort - will sort the list in ascending order

new_list.sort()
print("Sorted list: ", new_list)

# Reverse - will reverse the order of the list

new_list.reverse()
print("Reversed list: ", new_list)

print(new_list[0])
print(new_list[1])
print(new_list[2])
print(new_list[3])














