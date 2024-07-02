##Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

def replace_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)

def main():
    a = input("string: ")
    result = replace_with_colon(a)
    print(result)

if __name__ == "__main__":
    main()
