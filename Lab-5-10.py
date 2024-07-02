##Write a Python program to convert a given camel case string to snake case.
import re

def camel_to_snake(text):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, '_', text).lower()

def main():
    a = input("string: ")
    result = camel_to_snake(a)
    print(result)

if __name__ == "__main__":
    main()
