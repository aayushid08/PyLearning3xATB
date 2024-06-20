# Interview Question

# my_list = [1, "Pramod", 3, 4.5, 5]
# my_list.sort()  # '<' not supported between instances of 'str' and 'int'
# print(my_list)

squares = [1, 4, 9, 16, 25]

if not squares:             # not operator works with boolean. uska bolne ka matlab hai <if not "sqaures". sqaure ke jagha Aayushi bhi ho sakta hai>
    print("Not empty")      # if not 'Aayushi' matlab if not that list, print xyz. par Aayushi hai. vo true hai. isliye output is Empty
else:                       # it is like <if not squares: >> if not True >> that means >> if False <<
    print("Empty")          # not is always used with booleans
