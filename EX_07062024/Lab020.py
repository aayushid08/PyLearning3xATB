# in built function
# function -> for the repeated task we can use function
#print(), input(), type(), len(), range(),  max(), min(), id(), sum(), avg()

#Strings
name="Rahull"
print(name)
print(type(name))
print(id(name)) # id -> address of the variable where it is stored
print(len(name)) # len -> length of the string. Length always start with 1
name = name.upper() # upper -> convert string into upper case
name = name.lower() # lower -> convert string into lower case
a = name.count('l')
print(a)

#print the index
print(name[2])
print(name[6]) #string index out of range

#in python strings are Immutable in nature. we can not change the string.
# naam hai Rahul. 0 pe hai R. apne ko chmage karna hai H. to nahi ho payega.
name[0] = "H" # this is not possible. once it is created we can not change it. we can replace the whole namenbut not the one index value that is the one word.

