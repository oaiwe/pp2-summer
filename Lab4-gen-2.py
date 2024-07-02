#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def generate_even_numbers(N):
    for i in range(0, N+1, 2):
        yield i

N = int(input("enter the value: "))

even_numbers_generator = generate_even_numbers(N)

even_numbers = list(even_numbers_generator)

even_numbers_str = ", ".join(map(str, even_numbers))

print(even_numbers_str)
