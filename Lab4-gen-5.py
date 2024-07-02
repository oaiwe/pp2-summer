#Implement a generator that returns all numbers from (n) down to 0.
def countdown(N):
    for i in range(N, -1, -1):
        yield i

N = int(input("enter the value: "))

countdown_generator = countdown(N)

for number in countdown_generator:
    print(number)
