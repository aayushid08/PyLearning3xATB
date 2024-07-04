class Person:
    # Attribute
    name = None
    id = None
    phone = None
    city = None
    age = None

    # Behaviour
    def talk(self):  # No Arg -> No Return
        print("I can talk")

    def sleep(self, name):  # Arg with No Return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with Return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):  # No Arg with Return
        return "I am walking"


################END OF THE CLASS##############
################ OBJECTS #####################

#  Creating an object of the Person class
# objectRef = Object() -> ClassName()

suryaRef = Person()        # surya is indicator or obj ref. and object is person()
suryaRef.name = "Surya Prakash"  # . is used to access the attribute

# You can access the attributes of the object using the dot notation, e.g., surya.name


ayushi = Person()
ayushi.name = "Ayushi Tiwari"  # attribute
ayushi.talk()  # method / behaviour

janu = Person()
janu.sleep = "10 ghanta"  #attribute
janu.walk()  #method / behaviour
