# Multiple conditions  #commented this out because it is causing some issue in running the program as even after running 43 file, it is still running 42 itself
# aise time configuration ko clear karo and current file choose karo


# find the max between three numbers

#num1, num2, num3
#
#num1 > num2 and num1 > num3  -> num1
#num2 > num1 and num2 > num3  -> num2
#else num3

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

# this is for 3 numbers
# if num1 > num2 and num1 > num3:
#     print(f"{num1} is the greatest number")
# elif num2 > num1 and num2 > num3:             # elif can be more than one
#     print(f"{num2} is the greatest number")
# else:
#     print(f"{num3} is the greatest number")

# this is for 4 numbers
if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is the greatest number")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"{num2} is the greatest number")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"{num3} is the greatest number")
else:
    print(f"{num4} is the greatest number")




# agar if else nahi hona to use MAX

# max() try using it here if a chance

















