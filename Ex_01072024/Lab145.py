# Method Overloading:
# Python does not support method overloading
# in the traditional sense.
# overloading means same name but diffrent agruments

# Method - overloading - Not supported!

class MathUtil(object):
    def add(self, a, b=0, c=0):
        return a + b + c

    # def add(self,a,b):
    #     pass
    #
    # def add(self,a,b,c,d):
    #     pass

math = MathUtil()
op0 = math.add(1)
op1 = math.add(1, 2)
op2 = math.add(1, 2, 3)
print(op0)
print(op1)
print(op2)



    # def add(self,a,b):
    #     return a + b
    #
    # def add(self,a,b,c,d):
    #     return a + c

# in me se sab se pehele dusri wali method call hogi

# agar Method OL use karna bhi hai toh number of arguments change kar do, par tab bhi ye dikkat dega
# to hum kaise use kar sakte hai? by using the default parameters.
# line no 19 20 21
# so same name diffrent arguments. but overloding support nahi karta isliye apan ne ek method li aur diffrent parameters pass karvaye
# Overloading support nahi higa par default arguments me apan kaam chala sakte hai.
