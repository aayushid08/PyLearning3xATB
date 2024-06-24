# SET
# (12 , 34, 56) for unpacking this how many variables we need? -> 3 variables
a, b, c = (12, 34, 56) # tuple unpacking
# t.append()  # tuple are immutable in nature

t = (1, 2, 3, 4)
# agar tumko fir bhi append karna he hai to make new tuple
# new_tuple = t + (5, 6, 7)   # (1, 2, 3, 4, 5, 6, 7)
# new_tuple = t + (99,)  # (1, 2, 3, 4, 99)
# print(new_tuple)

# agar aise bhi nahi chahiye to tuple ko list me convert karo
new_list = list(t) # t ki value dekh upar. tuple lo list me banaya hai
print(new_list)
new_list.append(99)  # list ko append karo
new_tuple = tuple(new_list)  # aur list ko sidha tuple me convert karo
print(new_tuple)
