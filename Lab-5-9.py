##Write a Python program to insert spaces between words starting with capital letters.
import re

def spaces_between(text):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, ' ', text)

def main():
    a = input("string: ")
    result = spaces_between(a)
    print(result)

if __name__ == "__main__":
    main()
