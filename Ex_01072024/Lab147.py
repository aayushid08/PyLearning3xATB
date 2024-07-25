# Ecap
# Inheritance
# Poly ( method overiding)
# Class
# Object
# Constructor
# Self, super, __init__
# public, _ , __ private

# Abstraction
# Abstraction - OOPs
# Hiding the details and showing the what is required

from abc import ABC, abstractmethod


class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod             #father ki class hai aur father ne loan leke rakha hai s=aur aur son ko bharna padega
    def loan(self):
        pass


class Pramod(Father):
    def loan(self):
        print("Loan given")


pramod = Pramod("rancho")
pramod.loan()

# yaha loan uske baap ne liya hai par dena bete ko padh raha. its a HAVE TO relationship
# abstract methods are nothing but a forcefull methods to you.