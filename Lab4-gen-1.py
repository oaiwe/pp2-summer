#Create a generator that generates the squares of numbers up to some number N.
def generate_squares(N):
    for i in range(1, N + 1):
        yield i * i
        
N = int(input("enter the value:"))

squares_generator = generate_squares(N)

for square in squares_generator:
    print(square)
