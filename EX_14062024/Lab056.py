# With Argument, with return type:
# def add(a, b):
#     return a+b


def allowed_to_attend_python_class(name, password):
    if name == "Ayushi":
        if password == "secret":
            print("You are allowed to attend Python class")
    else:
        print("You are not allowed to attend Python class")

allowed_to_attend_python_class("Rohit","secret")

# Use of this is match case:

def allowed_to_attend_python_class(name):
    match name:
        case "DELL":
            print("Dell is allowed")
        case "Lenovo":
            print("Lenovo is allowed")
        case "ASUS":
            print("ASUS is allowed")
        case _:
            print("Na Behen Naa")


allowed_to_attend_python_class("DELL")

allowed_to_attend_python_class("Lenovo")

allowed_to_attend_python_class("apple")



