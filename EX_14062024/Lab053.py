# Multiple Conditions

# Switch in Java - In Python we use Match case

# number = int(input("Enter a number: "))
# # 3.10
# match number:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case _:                     # DEFAULT
#         print("Invalid number")

#String

# name = input("Enter a name: ")

# match name:
#     case "Jeene":
#         print("Jeene Mera OHOO")
#     case "Mera":
#         print("Mera Dil Lutiya OHOO")
#     case "Dil_lutiya":
#         print("Dil_lutiya OHOO")
#     case _:                     # DEFAULT
#         print("Sahi Gana Daliye")

#Browser Real life:

browser = input("Enter a browser: ")
browser = browser.lower()    # To convert the input to lower case. even if you enter the value in capital, it will have no issue
match browser:
    case "chrome":
        print("Execute the code of the chrome browser")
    case "firefox":
        print("Execute the code of the FireFox browser")
    case _:                     # DEFAULT
        print("No Idea")
