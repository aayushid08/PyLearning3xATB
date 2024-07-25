# Ecapsulation (data binding) jaise passowrd wala.. pehele password ka variable bahar hota tha .. fir private method ke andar bind kiya to secured hogaya
# Inheritance
# Polymorphism ( method overriding)
# Class
# Object
# Constructor
# Self, super, __init__
# public, _ , __ private

# Abstraction
# Abstraction - OOPs
# Hiding the details and showing what is required
# abstract means incomplete im a way

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod         #this incomplete function is given by animal
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog("rancho")
print(dog.sound())



cat = Cat("CAT")
print(cat.sound())

#how encap is diffrent from abstraction:
# >> encap means within the class, you create one class, in this class we have data members and methods.
#and we bind them together is  called encap. encap is within the class.
# >> abstraction >> present in diffrent class