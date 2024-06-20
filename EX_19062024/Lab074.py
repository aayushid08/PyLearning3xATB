# Functions scope with list

# set = {1, 2, 3, 4, 5}  # Set
# tuple = (1, 2, 3, 4, 5)  # Tuple
# list = [1, 2, 3, 4, 5]  # List

numbers = [1, 2, 3, 4, 5]  # List # Collection of items


# def do_something():
#     numbers.append(6)
#     print(numbers)
#
#
# do_something()

def do_something(pramod_list):  # pramod list isa kind of varibale "a" jisko aage function me value milegi "a = 16" ya "toppings = cheese" here toppings is pramod list and numbers is cheese
    pramod_list.append(6)       # we can append the values
    pramod_list[0] = 100        # we can change the values via index
    return pramod_list          # pramod_list is just a local variable within the program


l = do_something(numbers)   # we have call this function and we have pass list in the arguments. like it is toppings = cheese vs pramod list = numbers
print(l)

# l = do_something(pramod_list=numbers)   # similar to above. just clear karne ke liye bataya aise kar ke maine
# print(l)


# sab se pehele kya hoga. line by line execution l = do_something(numbers) ye execute hoga.
# ye numbers ki value upar jayegi (jaha fun define hua hai) arguments me. jaise numbers "cheese" hai aur vo value upar topings ke pass gai.
# vaise he humne yaha list pass kiya. list kya hai? numbers. List ki values kya hai [1 2 3]
# def me pehele kya execute hua? pramod_list.append(6). to list 6 se append ho jayegi
# fir index value change hui. vo change hojayegi
# fir badme kya hoga, list return hogi. kisko? l ko
# l = [100, 2, 3, 4, 5, 6]
# hum vo he list yane Numbers ko modify kar sakte the aur upar apan ne code bhi likha. par best practise is nayi list banao. pehele wali ko modify na karo.
# execution will always start from where the function is called
# defination would not have execuation. Calling the function will have execution

















