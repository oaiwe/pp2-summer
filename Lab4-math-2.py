##Write a Python program to calculate the area of a trapezoid.
#Height: 5
#Base, first value: 5
#Base, second value: 6
#Expected Output: 27.5
def trapezoid_area(a, b, h):
    return ((a + b) * h) / 2

a = float(input("the length of a: "))
b = float(input("the length of b: "))
h = float(input("the lenght of h: "))

area = trapezoid_area(a, b, h)
print(f"The area of the trapezoid is: {area}")
