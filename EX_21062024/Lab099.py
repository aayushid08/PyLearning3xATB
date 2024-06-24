#

def log_decorate(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")           # {func.__name__} - remember this
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper


@log_decorate
def add(a, b):
    return a + b


add(2, 3)


