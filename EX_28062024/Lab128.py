class MyClass:

    def __init__(self):
        self.name = "Amit"
        self._email = "amit@gmail.com"       # protected attribute

    def public_func(self):
        print("I am a public function")

    def __private_func(self):       # agar mai iska access he na du toh kya tum private method access kar paoge?
        # No. Kya private variable ko access kar paoge? No.
        print("I am a private function. you can only access it via another method, this is private")

    def public_fn_private(self):
        self.__private_func()
        print(self._email)
        print("I am calling a private function from a public function")


# security : not everyone can access __private but for it only public_fn_private(self): can access
a = MyClass()
a.public_func()
a.public_fn_private()


# I am a public function   a.public_func()
# I am a private function. you can only access it via another method, this is private #a.public_fn_private()
# amit@gmail.com        # print(self._email)
# I am calling a private function from a public function       # print("I am calling a........