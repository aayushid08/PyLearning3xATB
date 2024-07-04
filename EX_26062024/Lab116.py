class Dog:
    name = None  # see up
    id = None

    def __init__(self, name, id):
            self.name = name
            self.id = id

    def sleep(self):
        print("I am a Sleeeppp!!")

    def eat(self):
        print("Who is eating: " + self.name)



dog1 = Dog("Tuffy", 1)
dog2 = Dog("Buddy", 2)

#ABOVE 2 and BELOW 2 LINES
# jaise he object banta hai (dog()) vo automatically default constructor ko call karta hai
# yaha bhi dog() bante he vo init ke pass gaya. waha use dene ke liye 2 argumnets bhi the
# upar argument me suppose aara hai "Chaw", to "self.name" ki wajhse "name" ko value mil jayega.. ab "name = chaw" hai.
# ab dusra hai dog2.name = "Maww" hai vo current hojayega.
# matlb multiple object me jo bhi object call hoga.. name ki value uski hojayegi.



print(f'{dog1.name} has ID {dog1.id}')
print(f'{dog2.name} has ID {dog2.id}')

dog2.eat()


# self = for dog1, self will be giving the value to it. and same for dog2. means assigning the value to current.
# just like this keyword
#undertsand with the help of exapmle - see method eat() above
# matlb self keyword se: manlo maine obj1 bulaya jaise dog1. uski jo bhi value hai self se usko assign hojayegi. kyuki jo bhi current object ki value hogi vo self usko dedega.
# jaise ek obj ki value hai aayu dusre ki piyu. agar aayu ko bulaya to aayu set hoga.. piyu ko bulaya to piyu set hoga.

# real world example: mera business hai koi enquiry ke liye aaya hai aur mko system generated email bhejna hai.
# usko return email bhejna he hai to mko usko naam lagega. aur to aur har naye enquiry pe har naya naam hona chahiye.
# to kya karege iske code me this key word ya self use karege.
# jaise

# BOHOT IMP - Interview question
# hum init kyu use karte hai aur sadhi menthod kyu?
# purpose of init : Purpose: To initialize the instance's attributes when the object is created.
# jaise he object create hua aur usme koi argumnnet rahi, jaise ki CHAW, to chaw ke value pe action hoga(maan lo print hoga)
# aur normal method jo hai vo kabhi bhi jarurt padhne pe call ki jaati
# Yes, you can use a normal method to perform initialization-like tasks by using the self keyword to set instance attributes.
# However, it is important to note that this method will not be automatically called when an object is instantiated; you will need to call it explicitly.

















