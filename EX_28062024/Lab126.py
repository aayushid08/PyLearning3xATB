# Encapsulation -
# bind the data variables(any variable use to store data) with the methods
# Data Member - / Class Variables - jo class define hone ke bad hum define karte hai
# Methods - Def function within the class
# Wrapping or binding the data variables with the methods - Encapsulation.

# Hide the data members(class variables, instance variables) by using only the methods.

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when a Object is created")

    def change_password(self):
        self.password = "345"
# This is end of the class

xuv = Car()
xuv.password = "345"

#  in above example the password is revised after the object is created. This can be a security threat.
# So we defined the method and wrapped the data variable in it. So that only by calling the method itself we can change the password


# data variables: any variable use to store data
# Instance Variables: These are variables that are unique to each (object). They are defined within methods and prefixed with self
# Class Variables: These are variables that are shared among all (objects). They are defined within the class but outside any methods.
#
# Data Members: refer to variables that belong to a class.
# Instance Data Members: These are essentially instance variables, unique to each instance of a class>>(object).
#
#koi fark nahi hai.. variables he members hai