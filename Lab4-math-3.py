##Write a Python program to calculate the area of regular polygon.
#Input number of sides: 4
#Input the length of a side: 25
#The area of the polygon is: 625
import math

def regular_polygon_area(s, l):
    return int((s * l**2) / (4 * math.tan(math.pi / s)))

s = int(input("the number of sides: "))
l = float(input("the length of each side: "))

area = regular_polygon_area(s, l)
print(f"The area of the regular polygon is: {area}")
