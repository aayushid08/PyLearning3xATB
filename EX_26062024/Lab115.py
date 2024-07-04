# name = "Amit" # pehelei baat python line by line interprete karta hai
#usko kuch na kuch value chahiye. agar amit dege to hard coded hojayega.
# is liye None dete hai

class Dog:
    name = None  # see up
    id = None

    def __init__(self, name, id):  # in java this name was the same as class name.
        self.name = name  # __ double underscore means private in nature. Which is only available in class
        self.id = id  # self is similar to THIS keyword in java

        #self means "this belongs to me" >> here this belongs to dog class

    #Constuctor - > init -> initialize
    # use to initialize the values of the instance variable (Attributes)

    def sleep(self):
        print("I am a Sleeeppp!!")


dog1 = Dog()
print(dog1.name)  #None
dog1.name = "Tuffy"
print(dog1.name)  # Tuffy
dog1.sleep()  # I am a Sleeeppp!!

dog2 = Dog()
print(dog2.name)  # None
dog2.name = "Buddy"
print(dog2.name)  # Buddy
dog2.sleep()  # I am a Sleeeppp!!

# there is a function which will automatically called when you run dog1 or dog2 = person()
# The function is __init__ This is actually a constructor


# Why to use constructor:
# suppose: there is a function which is automatically called when you create an object of the class
# in that function we can set the value of name.
# the function is init function: __init__ >> __ means private in nature and only available in class
# in java we have this default constructor was same as the class name.




