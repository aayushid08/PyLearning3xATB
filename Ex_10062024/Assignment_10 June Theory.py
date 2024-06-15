# Task #1
# Explain the difference between the = operator and the == operator in Python.
# What does the ** operator do in Python, and how is it used?
# What does the ^ operator do in Python, and in what context is it commonly used?

# Task #2
# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
# Push the code to Github.com



# Explain the difference between the = operator and the == operator in Python.
# Answer:
# = is for assignment.
# == is for comparison.
# = is used to assign a value to a variable, whereas == is used to compare the values of two variables.
# Examples:
# a = 2 means that the variable a is a container that holds the value 2.
# a == 2 means that we are checking if the value of a is equal to 2.
# if we will print "a" with = it will give the exact value
# if we will print "a" with ==  it will give the boolean value

a = 2
print(a)  # Output: 2

a == 2
print(a == 2)  # Output: True

a == 3
print(a == 3)  # Output: False # kyuki a ki value upar he 2 define kari hui hai


# What does the ** operator do in Python, and how is it used?
# Answer:
# if we want to calculate the power of a number, we use ** operator. For example, 2**3 means that we want to calculate the cube of 2.

# print(2 ** 3)  # Output: 8
x = (int(input("Enter a number:")))
y = (int(input("Enter a power:")))
print("Calculation of the number to the power is:", x**y)

# What does the ^ operator do in Python, and in what context is it commonly used?

# Answer: ^ it represents the XOR gate. its a bitwise operator. it returns 1 if the bits are different and 0 if the bits are the same.
# For example, 5^3 means that we want to compare the binary representation of 5 and 3.

x = 5
y = 3
print(x ^ y)  # Output: 6

# This means that the binary representation of 5 is 101, and the binary representation of 3 is 011. When we XOR these two numbers, we get 110, which is 6 in decimal representation. This is because the bits are different for each position.
# binary me convert karna ho khudse to use rapid tables to convert from decimal to binary and vice versa








