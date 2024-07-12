# encapsulation is hiding
# here it is hiding the balance
# and bundling the variables with methods
# getter and setter can be used


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, balance):
        self.balance += balance

    def __withdraw(self, balance):
        self.balance -= balance

    def __show_balance(self):
        print("Your Balance is ", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")

    def if_you_are_auth_user(self, auth, balance):
        if auth:
            self.__withdraw(balance=balance)
        else:
            print("Not Allowed")


jp_chase = BankAccount()
jp_chase.deposit(100)

secret_pass = input("Enter your PIN to see Balance")
if secret_pass == "1234":
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth(False)

secret_pass = input("Enter your PIN to Withdraw")
your_amount = int(input("Enter your amount to Withdraw"))
if secret_pass == "1234":
    jp_chase.if_you_are_auth_user(True, balance=your_amount)
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth_user(False)















# boi = BankAccount()
#
# m1 = input("Please let us know how we can help you. (Deposit / Check Balance / Withdraw): ")
# if m1 == "Withdraw":
#     withdraw = input("Do you want to withdraw:(yes/no)  ")
#     if withdraw == 'yes':
#         secret_pass = input("Enter your PIN")
#         if secret_pass == "1234567890":
#             boi.if_you_are_auth_user(True)
#         else:
#             boi.if_you_are_auth_user(False)
#     else:
#         print("Wrong value entered")
# elif m1 == "Check Balance":
#     secret_pass = input("Enter your PIN")
#     if secret_pass == "1234567890":
#         boi.if_you_are_auth(True)
#     else:
#         boi.if_you_are_auth(False)
# elif m1 == "Deposit":
#     boi.deposit(900)
# else:
#     print("Access Denied")









# print(boi.balance)        #isme hai he gadbad

# boi.if_you_are_auth(True)
# boi.if_you_are_auth(False)
# boi.if_you_are_auth_user(True, 101)
# boi.if_you_are_auth(True)

#apan aise bhi kar sakte


#left space for modification
# first user will see deposite, withdraw and check balance
# agar deposite bola to call deposite else withdraw ke liye maine niche he mention kiya hai








# boi.show_balance()    # abhi you cannot access this
#
# boi.withdraw(99)        # abhi you cannot access this
# boi.show_balance()      # abhi you cannot access this
#
# boi.withdraw(50)        # abhi you cannot access this
# boi.show_balance()      # abhi you cannot access this



















