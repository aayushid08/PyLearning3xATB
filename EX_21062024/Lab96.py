# Decorators - a function that takes another function as an argument and extends its functionality
# it returns a new function with extended functionality, without modifying the original function

# we use decorators to decorate a function with additional functionality by extending its behaviour

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")      # ye pehele execute hoga. Kyuki python line by line execute hota hai aur pehele hai wrapper.
        func()                           # ye function hai jo hum mainly call kar rahe hai
        print("Something is happening after the function is called.")       # aur ye third no pe execute hoga after humara main function
    return wrapper

@my_decorator
def say_hello():    # this function will go to  "def my_decorator(func):"  and call wrapper()
    print("Say Hello")


say_hello()

