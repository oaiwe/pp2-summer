#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(N):
    for i in range(0, N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

N = int(input("enter the value: "))

divisible_generator = divisible_by_3_and_4(N)

for number in divisible_generator:
    print(number)
