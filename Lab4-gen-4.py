#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("enter the value a: "))
b = int(input("enter the value b: "))

squares_generator = squares(a, b)

for square in squares_generator:
    print(square)
