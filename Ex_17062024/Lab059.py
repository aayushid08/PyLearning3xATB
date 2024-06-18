# With Argument without return type
# Argument le raha hai par return nahi kar raha

def say_hello_arg(name):
    print("Hello", name)


say_hello_arg("Alice")  # calling the function with argument
say_hello_arg("Ayushi")

# ye bhi return karne wala nahi hai

result = say_hello_arg("Ayushi")
print(result)  # None


####

# EXAMPLE WITH DEFAULT ARGUMENT

def say_hello_arg_default(name="Ayushi"):  # no return with argument
    print("Hello", name)

    # no return type with default argumenty


say_hello_arg_default()  # agar mai isko directly call karti hu aur koi argument pass nahi karti tab bhi ye return karega
say_hello_arg_default("Diksha")  # default arg ko overide karega
say_hello_arg_default(name="Dhruv")  # aise bhi lega

say_hello_arg_default("Diksha", "Dhruv")  # ye nahi lega


####################################################################


# With Argumnet with return type
# Argument le raha hai aur return kar raha hai

def sum_number_argument_ret(a, b):
    return a + b


sum_number_argument_ret(2, 3)  # calling the function with argument and return type
# in this case you should know what and where is a and b.
# sum_number_argument_ret(a = 41, b = 63):


# #check if it returns or not
# result = sum_number_argument_ret(2, 3)
# print(result)  # 5

############################################################# PTO

# Without Argument with return type
# Argument nahi le raha hai aur return kar raha hai
