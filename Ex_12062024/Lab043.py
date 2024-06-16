# LOOP
# repeat a block of code multiple times

# Print hello world for 5 times

# SAADHA NORMAL but not good approach

# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')

# GOOD APPROACH

for i in range(5):   # i is just a variable aur output idhar 1 to 5 take hota tha
    print('Hello world') # but 1 to 5 tak humne hello world print kara diya

for i in range(1, 5):
    print(i)  # prints 0,1,2,3,4

for amit in range(1, 5):    # amit is just a variable
    print("amit", amit)

# Range has a mechanism (Start, Stop, Step)

for i in range(1, 10, 2):  # 1 is start | 10 is stop | 2 is step matlab 2 2 number ke gap se num print hoge. jaise ki even numbers
    print("odd, matlab he 2 ke gaps se", i)

for i in range(1, 10, 3):
    print("3 ke gap se", i)

for i in range(1, 10, 1):
    print("koi gap he nahi hoga", i)

# for i in range(1, 10, -1):         # aise kuch print nahi hota
#     print("reverse order", i)

for i in range(10, 1, -1):
    print("reverse order", i)






