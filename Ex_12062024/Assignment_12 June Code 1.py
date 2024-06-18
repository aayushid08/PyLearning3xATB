# ✅ 1. Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = Leap year

# year = int(input("Enter a number: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is leap year")
# else:
#     print(f"{year} is not a leap year")


########################################

# other way what Pramod explained

year = 2028

(year % 4 == 0)
(year % 100 != 0)
(year % 400 == 0)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")








