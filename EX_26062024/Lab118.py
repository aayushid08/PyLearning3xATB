class Calc:

    def __init__(self):
        print("Hello DC")

    def sum(self, a, b):
        return a+b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

object_ref = Calc()
result = object_ref.sum(10, 20)  # IF WE USE Functions/METHOD WE NEED TO GIVE ARG HERE
print(f'The sum is : {result}')
