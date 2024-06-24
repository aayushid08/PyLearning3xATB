x = 10

# tuple's each item can be assigned to a different variable, unpacking ka error deta hai nahi to. unpacking - assigning to a diffrent variable
q, w, e = (11, 22, 56)
print(q)
print(w)
print(e)

# search in tuple
cities = ("London", "New York", "Paris", "Berlin")
print("Berlin" in cities) # True
print("Moskow" in cities) # False
print("Moskow" not in cities) # True


# # (12 , 34, 56) for unpacking this how many variables we need? -> 3 variables
# a, b, c = (12, 34, 56) # tuple unpacking