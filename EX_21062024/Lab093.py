
# subset - where element of set2 is already the part of set1, it will give a boolean value
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
subset = set2.issubset(set1)
print(subset)                   # True

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4, 8}
subset = set2.issubset(set1)
print(subset)                   # False