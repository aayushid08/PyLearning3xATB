# Not a secure class
# functions within the class can access the private varibles.
# like babya(public method) at my home(class) can access my laptop (private varibles)

class Car:
    name = None

    def __init__(self):
        self.public_var = "public"          # no underscore
        self._protected_var = "protected123"   # single underscore
        self.__private__var = "private456"     # double underscore

    def __private_method(self):
        if self._protected_var == ("123"):
            print("I am protected variable allowed in private")
        print("protected")

    def printName(self):
        if self.__private__var == ("123"):
            print("I am private variable allowed in public 123")
        print("I am allowed")

# end of the class

alto = Car()
alto.printName()
#alto.__private_method()    # this is not allowed

# if object alto cannot access the private method than who can access it
# answer is the class itself
#Car.__private_method(alto)    # this is allowed

# also functions within the class can access the private variables
# means __private sirf class ke andar he accessiable hai aur vo bhi public method se..
# class ka class ke andar private protected access karna chalta hai par par bahar wale ka nahi
# private things are allowed only in the class
# public are availabe everywhere
# protected are allowed only in the module