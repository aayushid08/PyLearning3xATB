t = ("Aayushi", "for", "Aayushi")
print(set(t)) # Converting tuple into set. set function is used to remove duplicates from the tuple

#just revise
# print(t.count("Aayushi")) # it will return the number of times "Aayushi" appears in the tuple
#print("Aayushi" in t)  # it will return True if "Aayushi" is present in the tuple, otherwise False

# union of sets - where elements of two sets will combine and form new set
set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)        # {1, 2, 3, 4, 5, 6}  # 1 U 2
print(my_set)

# intersection of sets - where common elements between two sets will be extracted and formed into a new set
set1 = {1, 2, 3, 4, 6, 8}
set2 = {2, 3, 4, 5, 3, 6}
my_set = set1.intersection(set2)         # {2, 3, 4, 6}  # 1 & 2
print(my_set)

# difference of sets - where elements of one set which are not present in another set will be extracted and formed into a new set
set1 = {1, 2, 3, 4, 6, 8}
set2 = {2, 3, 4, 5, 3, 6}
my_set = set1.difference(set2)      # {1, 8}  # 1 - 2
print(my_set)


















