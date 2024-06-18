#def make_pizza(*topings):
# """Print the list of toppings that have been requested."""
    # print("\nMaking a pizza with the following toppings:")
    # for topping in topings:
    #     print(f"- {topping}")

# * means n number of arguments
def make_pizza(*toppings):
    print(toppings)
    for topin in toppings:
        print(topin)

pramod = make_pizza("pepperoni")
bhargav = make_pizza("mushrooms", "green peppers", "extra cheese")
ayushi = make_pizza("onions", "pineapple", "extra cheese",  "sausage",  "bell peppers")


# *args list aur tupple dono ke jaise lagte par list aur tupple fark sirf itna hai:
# list are mutable and tupple are immutable in nature

# tupple = ("Pramod",  "Amit", "Lucky")
# tupple [0] = "Ria"  # yaha pramod replace NAHI hoga ria se. Kyuki mutable nahi hai
# print(tupple)

# aur agar if it is a list then:
list = ["Pramod", "Amit", "Lucky"]
list[0] = "Ria"     #  yaha pramod replace hoga ria se
print(list)


# FARK SIRF () [] KA HAI.  (TUPPLE KA U) [LIST KA L]