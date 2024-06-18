# *args matlab we can type n number of arguments
# args are taken irrespective of their data types

#print("Sab", "First Class", "Hai")

#
# def sum3(a, b, c):
#     return a + b + c
#
# result = sum3(2, 3, 4)
# print(result)  # Output: 9

# agar default values bhi dedege aur function ko call without arg karege tab bhi chalega

def sum3(a=8, b=10, c=20):
    return a + b + c

# Normal
# result = sum3()
# print(result)  # Output: 38

# agar default value dene ke bad bhi koi dusri arg dege to vo override karega usko
# result = sum3(2, 3, 4)
# print(result)  # Output: 9

# is bar 2 he argument dege to tisri jo default hai vo lelega

result = sum3(2, 3)
print(result)
