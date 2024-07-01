# ✅ Right Triangle Star Pattern
# n = 5
# *
# **
# ***
# ****
# *****


#n = input("Enter the number of rows: ")

# for i in range(1, int(n) + 1):          # suppose the range starts with 1 here, and the range given as 4 so it will print the iteams from 0 to 3. is liye apan n + 1 kar rahe
#     print("*" * i)

# output:
# *
# **
# ***
# ****


# for i in range(int(n)+1, 0, -1):          #suppose = int(n)+1 = 5 hai. ToH 5 se leke 0 tak -1 kar kar ke
#     print("*" * i)
#
# output:
# *****
# ****
# ***
# **
# *


# for i in range(int(n)+1, 0, -1):
#      print("o" * i)
# output:
# ooooo
# oooo
# ooo
# oo
# o


#FAILED
# for i in range(1, int(n) + 1):
#     spaces = int(n) - i
#     stars = i
#     print(" " * spaces, end="")
#     print("*" * stars)

##################################

# for i in range(int(n), 0, -1):
#     spaces = int(n) - i
#     stars = i
#     print(" " * spaces + "*" * stars)

#  output:
#     *
#    **
#   ***
#  ****
# *****


# remember to print reverse of numbers:

# for i in range(5, 0, -1):
#     print("*" * i)


# remeber to print even number

# for i in range(0, 10, 2):    # 0 se leke 10 tak 2 ki gap se
#     print("*" * i)