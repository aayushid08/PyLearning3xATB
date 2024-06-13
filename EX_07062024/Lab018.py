#Strings

# Bunch of characters
# '', "", """ """, ''' '''

name = "Amit"
print(name)

name = 'Amit'
print(name)

name = """Amit
i am good
i got 15 LPA package
i made my family proud
Har Har Modi"""   # when you have long string you can use this """
print(name)

name = '''Amit'''
print(name)

##################
#now the below one id directory. after writing this in single or double quotes it is still showing as some error kind of yellow line.
#what is expected here? it means that "\" is a kind of new line character. for escape character we trued using "/" but it is not working.
# how to fix this? use raw string "r". This is how we give directory path in python.


#raw string
dir= r"C:\Users\amit\Desktop"
print(dir)

# Format of the string by f
f_n = "Radha"
l_n = "Vallabh"
#diffrent ways to print the string
print(f_n,l_n)
print(f_n,"",l_n)
print(f_n + " " + l_n)
# f is use for formating like r (raw string) and it will replace the f_n and l_n with the value.
# whenever {} will be there it will replace with the value. -> placeholders
print('Your full name is{f_n}{l_n}')














