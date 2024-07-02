##Write a Python program to calculate the area of a parallelogram.
#Length of base: 5
#Height of parallelogram: 6
#Expected Output: 30.0
def parallelogram_area(base, height):
    return base * height

# Example usage
base = float(input("Enter the length of the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

area = parallelogram_area(base, height)
print(f"The area of the parallelogram is: {area}")
