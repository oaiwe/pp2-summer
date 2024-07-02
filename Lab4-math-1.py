##Write a Python program to convert degree to radian.
#Input degree: 15
#Output radian: 0.261904
import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degrees = float(input("Input degrees: "))
radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is equal to {radians:.6f} radians")
