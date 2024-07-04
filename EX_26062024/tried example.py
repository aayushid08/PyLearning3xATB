class Email:
    name = None         # instance variable
    game = None         # instance variable

    def __init__(self, name = None):       # Constructors does not have a return type
        self.name = name

    def email_name(self):
        print("Kisko mail bhejna hai: ", self.name)



admi1 = Email("Komal")
print(f'name is : {admi1.name}')
admi2 = Email("Rahul")
print(f'name is : {admi2.name}')

email_name = admi1.email_name()

# INTERVIEW QUESTIONS:
# in which line constructor is called >> Line 5
# what is self : >> current object
# which one is the method : >> Line 5 and Line 8
# which line has the instance variable >> Line 2 and 3


# Diffrence between Constructors and Methods
# Initialization vs. Behavior: Constructors are used for initializing new objects, while methods define the behavior of those objects.
# Automatic Call vs. Manual Call: Constructors are called automatically when a new object is created, whereas methods are called manually on the object instances.
# Naming: The constructor has a fixed name (__init__), while methods can have any valid function name.
# Role in Class: The constructor is crucial for setting up an object, ensuring it has the necessary attributes. Methods are essential for defining what the object can do.







