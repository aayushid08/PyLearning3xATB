class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message #+ "Aayu it got failed"
        super().__init__(message)


balance = 100
withdraw = int(input("Enter the amount!"))
if withdraw > balance:
    raise MyCustomException("Bal is Low!!")
    # raise is use when you know that it is going to fail
else:
    print("Remain Bal ", (balance - withdraw))


# The `raise` keyword is used to trigger an exception in Python.
# It stops the normal flow of the program and transfers control to the nearest enclosing exception handler (try-except block).