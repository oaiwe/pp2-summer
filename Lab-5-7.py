##Write a python program to convert snake case string to camel case string.
def snake_to_camel(text):
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def main():
    a = input("string: ")
    result = snake_to_camel(a)
    print(result)

if __name__ == "__main__":
    main()
