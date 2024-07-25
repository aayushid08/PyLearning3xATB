# Method Overriding - Same name in the parent and child
# child always override the parent functions
# super means call my parent function

class Father:
    def home(self):
        print("1BHK")

class Son(Father):
    def home(self):         # method overload hogai.. you cam see the sign too in left. matlab dono bhi class me same method name.
        super().home()      # agar sirf home hota aur super nahi hota toh to current class ki he method call hoti.. par super use kiya toh uske uper ki class ka method call hoga. aur fir iska method call hoga. NICHE dekh
        print("No House")


pramod = Son()
pramod.home()

# super keyword: se sirf uske upar ka method call hoga baki uske bhi upar ka nahi. son sper is father and father ka GF
# baki upar dekh