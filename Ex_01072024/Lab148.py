
from abc import ABC, abstractmethod
class PyATB(ABC):

    @abstractmethod         # Python batch khol rakhi hai fees usne leni padti, isliye shubham ko fees bharni padegi
    def payFee(self):
        pass

    def enrolled(self):
        print("Enrolled")


class Shubham(PyATB):

    def payFee(self):       # kya shuham be called directly. pehele usko fees bharni paedgi... ye he abstract methods hai. force to pay the fees
        print("Paid")


shubham = Shubham()
shubham.enrolled()
