name = "Aayushi"
print(type(name))
#123 = 456 nahi ho sakta. Variable names as integer nahi ho sakta.
#varibale name shoukd be start from A_-Z or a-z.
# should not be start from number
# shoukd not be any special character.
# should not be any keyword or any space.

#keywords ? >> Reserved words.

import keyword
print(keyword.kwlist)

# so there are 35 keywords as follows
#'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# we cannot do and = 123 as and is reserved. and will become blue

# No special character is allowed. just "_"
# spcae is also not allowed.
first_name = "Aayushi"
# first name "Aayushi"   // Not allowed

# python loves the snake case
# In Python, snake case is a naming convention where words are written in lowercase and separated by underscores (_). It is commonly used for variable names and function names.
# snake case = every space is replaced by under score

#java loves Camel Case and python Snake Case
#camel_case_variable = "totalPrice"
#snake_case_variable = camel_to_snake