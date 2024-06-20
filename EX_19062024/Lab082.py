# list to double the elements

# list1 = [1,2,3,4,5]
# print(list1*2)            # isse list 2 bar print ho jaayega

# list1 = [1, 2, 3, 4, 5]
# for i in list1:
#     print(i*2)              # bad idea. this is doubleing it but not printing in a list.


# we have to store the list in the temporary variable and then print it.

#list = [1, 2, 3, 4, 5]
# temp_list = []                   # means list is empty
# for i in list:
#     temp = i*2
#     temp_list.append(temp)
# print(temp_list)

#it is always advisibe to create new list


# double the list item without using inbuilt or append function
# MAP()
# for that we need to use Map()
# 1. Takes each item form the list.
# 2. Execute the function on it.
# 3. Return same number of elements (list).
# in map we use key and value Map(key, value)

my_list = [1, 2, 3, 4, 5]
def double_item(num):
    return num*2

my_list = [1, 2, 3, 4, 5]
double_list = list(map(double_item, my_list))
print(double_list)

# map ke andar double_item function hai, vo upar jayega def ke double item ke pass.
# list me ki pehele chiz, 1, uska double hojayega.
# one by one element it will pick and it will start executing for each element for execute double item.
# double_ item is a function

# lamda expression

double_list = list(map(lambda num: num ** 2, my_list))
print(double_list)

# see the video for this - 19 june















