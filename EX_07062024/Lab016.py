# Take 2 int numbers from the user and add them
# need to use input() function

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print("The result is: ", result)

##### OR another way to write it #####

num1 = (input("Enter first number: "))
num2 = (input("Enter second number: "))
result = int(num1) + int(num2)
print("The result is: ", result)

# in the above progran we have done type conversion, so basically it has added two number. if you will remove int from it, it will just concatinate it.
# so to avoid this we have to use int() function.
# int() function will convert the string to integer.
# + -> with int is sum operation
# + -> with str is concatination operation
# int to string -> str() function
# string to int -> int() function

# type conversion - string to integer -> int()