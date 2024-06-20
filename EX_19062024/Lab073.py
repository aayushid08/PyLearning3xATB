def outer():
    varl = 30

    def inner():
        print(varl)

    inner()


outer()

# How Python looks towards it

# >> first it will interpret line by line
# >> pehele dekhega ki outer function hai
# >> outer function me mila varl = 30
# >> aur dekha outer what you have? that is defination of inner function but as of now it will not execute anything
# >> seeing "inner () " only inner function will execute
# >> but it will still not execute until you execute outer function
# >> matlab dono ko execute hona hoga.
# >> inner function thing is a private thing. print ko tum access nahi kar sakte jab tak inner ko call nahi karoge.
# >> inner functions ar just to do some inner functionalities. and there can be n number of inner functions.
# >> inner functions can have access to the outer function variables but would send back the information.
# like son gets everything for father but son doesnt share anything with father.



