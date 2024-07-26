# The `MyCustomException` class is a custom exception handler, providing more specific and meaningful error handling compared to built-in exceptions.
# It is not used instead of try-catch but rather within a try-catch block to handle specific errors more clearly.

class MyCustomException(Exception):  #if i want to make my own exception,
                                    # we can inherit exception and directly use it.
    def __init__(self, message):
        self.message = message
        super().__init__(message)      # this is nothing but calling the parents constructor, parent will also have the constructor

#matlab puri ki puri exception wali class ko yaha bulana hai.. parent bol ke child ke andar.. aur usko constructor ko bhi bula lo
# matlav vo exception class he ban gai puri.. sirf naam mycutom diya hai.. aur child ke form me hai

balance = 100
withdraw = int(input("Enter the amount!"))
if withdraw > balance:
    raise Exception("Bal is Low!!")     #balance is low
else:
    print("Remain Bal ", (balance - withdraw))