# Difference between map and filters
# MAP: Returns Normal Numbers
# MAP: It picks 1 item and apply the function : return the same numbers of elements.
# yaha list ki value jitni ki utni he milegi
# Filters: Function calculate True or False: suppose it will pick item "m", if it is true - keep it, if it is false remove it.
# yaha list ki value kam hojayegi


# map - return numbers
# pick 1 item and apply the function
# give the same number of elements  <<<<<<<<<<<<<<<<<<<<

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def double_me(n):
#     return n * 2


# new_list_double = map(double_me, numbers)
new_list_double = map(lambda n: n * 2, numbers)
print(list(new_list_double))


# Filters - return function true or false
# pick item m if true keep it, false, remove it  <<<<<<<<<<<<<<<<<<<<<
# it can give less number of items as compared to actual list

def even_giver(n):
    return n % 2 == 0


# new_filteted_list = list(filter(even_giver, numbers))
new_filteted_list = list(filter(lambda x: x % 2 == 0, numbers))
print(list(filter(lambda x: x % 2 == 0, numbers)))

#suppose i want to wrute the code in one line

# print(list(filter(lambda n: n % 2 == 0, numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))