class Parent:
    def __init__(self):
        print("I am Parent")


class Son(Parent):
    def __init__(self):
        super().__init__()      #it can call parent. ie fun on line 3 and and print on  line4


s = Son()