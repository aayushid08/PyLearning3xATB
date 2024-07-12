class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100        #maanlo current balance - aise he abhi ke liye

    def public_fn(self):            # apan public ke andar private is liye he banate hai kyuki private finction tum directly access nahi kar sakte.
        print(self.__private_var)   # to usko koi public function me dala padta.  aur vo pulic function ko call kar private method call karege

    def deposit(self, amount):
        self.balance += amount      # balance = balance + amount

    def withdraw(self, amount):
        self.balance -= amount      # balance = balance - amount

    def show_balance(self):
        print("Your Balance is ", self.balance)

jp_chase = BankAccount()
print(jp_chase.balance)

jp_chase.deposit(101)
jp_chase.show_balance()

jp_chase.deposit(99)
jp_chase.show_balance()

jp_chase.withdraw(199)
jp_chase.show_balance()

# jp_chase.public_fn()

# balance dalna to sahi hai lekin withdraw to aise aasani se hora hai ki koi authentication nahi kuch nahi koi security nhai
# very poor encapsulation















