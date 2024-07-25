# Multiple Inheritance

class Father:
    def father_money(self):
        return "5"

    def home(self):
        return "This is from the Father"


class Mother:
    def mother_money(self):
        return "2"

    def home(self):
        return "This is from the Mother"


class Son(Father, Mother):

    pass
    # def home(self):
    #     return "This is for the Son"



# Problem - Diamond Problem - Java
# Python - Multiple Inheritance
# F,M -> S (agar son ke pass home jaisi koi method nahi hai, aur mother father me se dono ke pass HOme hai.. ab kisko bulana. toh jiska pehele argument hoga usko)

son = Son()
son.father_money()
son.mother_money()
print(son.home()) # Method Resolution (home Mother Father aur Son tino pe pass hai.. Whom to call. LOCAL HAS THE PREFRENCE)