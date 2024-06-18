# with argument with return type
def add(a, b, c):
    return a + b + c            # return the value after summing them irrespective of datatypes


# print(add(2, 4, 6))

result = add(2, 3, 4)
# result = add(a=2, b=3, c=4)
# result = add(c=4, a=2, b=3)
print(result)  # Output: 9

#can you print after the return statement
#yes we can print after the return statement but it will not be executed

# def add(a, b, c):
#     return a + b + c
#     print("Hello") # This line will not be executed


# print("Hello")     # This will be execuated as it is outside the function


# agar define niche kar rahe aur print upar kar rahe to nahi chalega. kyuki python is a interpreture language


# but we can print the value between def and return
# def add(a, b, c):
#     print("Hello")
#     return a + b + c


# if we do not pass any argument or jyada ke arguments, #error#
# jab return type nahi rahega to None print karega
# *args matlab we can type n number of arguments







