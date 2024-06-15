# Remember "is" and "==" are diffrent operators. :"is" checks if two variables refer to the same object, while "==" checks if the values are the same.
x = [1, 2, 3]
y = x
print(y is x)  # True
print(y == x)  # True
z = [1, 2, 3]
print(z is x)  # False
print(z == x)  # True


# Using if
a = 10
b = 20
# "a if condition else b" - if the condition is true, it returns "a", otherwise it returns "b"
print("a is greater" if x > y else "b is greater")

############ Ternery operator ########## Condition
Aayu = 10
Babu = 20

# x > y -> do something - print("Aayu"
# x < y -> do something else - print("Babu")

print ("Aayu" if Aayu > Babu else "Babu") # single line


# other way

if Aayu > Baby:
    print("Aayu is greater")
else :
    print("Babu is greater")
















