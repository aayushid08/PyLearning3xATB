# # function = lamda argument:expression
# def find_odd_even(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# o = find_odd_even(11)
# print(o)

# using lambda
num = int(input("Enter a number: "))

o = lambda num: "Even" if num % 2 == 0 else "Odd"
print(o(num))

