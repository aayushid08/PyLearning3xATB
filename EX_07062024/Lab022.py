val = None
#data type - NoneType
print(val)
# Nothing
# None is not a default value
# None is not 0
# None is not an empty string
# None is not the same as false

# No operations are allowed with None
# val = val + 1
# print(val)

num = 1
num = num + 1 # idhar operations ho rahe hai par udhar None ke sath nahi ho rahe hai.
num += 1
print(num)

# None is use to initialize the value.

name = None   # a seperate memory is alloted for None.
print(name)
print(id(name))  # None ki memory bhi rahegi
print(type(name)) # None ka type None he rahega
name = "Rahul" # Rahul ke liye bhi ek seperate memory is alloted.
               # kuch ek array hoga usme index number hoge.
               # pehele jab humne name = None likha tab memory pointed None ko thi.
               # jab name = Rahul likha gaye vo memory none se hat ke Rahul ko point ho gai.
print(name)
print(id(name))

name = "" # empty string -> isko bhi memory lagti hai
print(name)
print(id(name))

