# Task #2
# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

# Discribed in normal
num = 2
sq_num = num ** 2
cube_num = num ** 3
print("Square of 2 is:",  sq_num, "Cube of 2 is:", cube_num)

# Discribed using f string

num2 = 4
sq_num2 = num2 ** 2
cube_num2 = num2 ** 3
print(f"Square of {num2} is {sq_num2} and Cube of {num2} is {cube_num2}")

# describe using format outside

num3 = 8
sq_num3 = num3 ** 2
cube_num3 = num3 ** 3
print("Square of {} is {} and Cube of {} is {}".format(num3, sq_num3, num3, cube_num3))  # ye thoda dyan de syntax pe. values outside define karni hai aur format ke pehele "." lagana hai


# taking input from user
num4 = (int(input("Enter the number:\n")))
num5 = (int(input("Enter the power:\n")))
print(num4, "to the power", num5, "is:", num4**num5)




