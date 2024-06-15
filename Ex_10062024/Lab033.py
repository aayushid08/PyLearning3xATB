# program for area of circle
import math

# peheli baat
# Program - Calculate the area of a circle
# input -> radius
# output -> area of the circle

# dusri baat
# data types kya rahege
# input kya hoga -> int ot float -> isme se hum float he lege
#  output kya hoga -> float

# Core Logic -> pi * r * r
math.pi
radius = input("enter the radius:")
radius = float(radius)
area = math.pi * radius * radius
print("Area of circle is:", area)

# other way

radius = float(input("Enter the radius: "))
area = math.pi * radius * radius
area2 = math.pi * radius ** 2
area3 = math.pi * pow(radius, 2)
print("Area of circle is:", area, area2, area3)

# other way in one line

radius = float(input("Enter the radius: "))
print("Area of circle is:", math.pi * radius ** 2)






