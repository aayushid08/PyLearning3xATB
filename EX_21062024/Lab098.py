def decorator1(func):
    def wrapper():
        print("decorator 1")
        func()
    return wrapper  # No need for ()

def decorator2(func):
    def wrapper():
        print("decorator 2")
        func()
    return wrapper  # No need for ()

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()  # This call is necessary to execute the function and see the output



# inbuilt decorator list:
# to mark this methods decorators
# staticmethod decorator.
# peoperty
# value.setter
# login purpose

# decorators ince created can be used by many functions