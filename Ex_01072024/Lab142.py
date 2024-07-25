# Interview question: What is the output for this and what is this type of inheritance

class GF:
    def car(self):
        return "Old car"

class F(GF):
    def car(self):
        return "honda civic"

class S(F):
    def car(self):
        return "Lambo"

son = S()
gf = GF()
print(gf.car())     #same method names are not allowed. 4 aur 10 pe ek he method hai.. method override hogai. isliye son usko use nahi kar payega. isly GF ka naya object banana hoga agar gf ka use karna hai to
print(son.car())
