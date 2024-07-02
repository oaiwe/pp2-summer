##Write a Python program to split a string at uppercase letters.
import re

def split_at_uppercase(text):
    pattern = r'(?=[A-Z])'
    return re.split(pattern, text)

def main():
    a = input("string: ")
    result = split_at_uppercase(a)
    print(result)

if __name__ == "__main__":
    main()
