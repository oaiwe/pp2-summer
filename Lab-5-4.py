##Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

def uppercase_with_lowercase(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

def main():
    a = input("string: ")
    matches = uppercase_with_lowercase(a)
    if matches:
        print(matches)
    else:
        print("No sequences")

if __name__ == "__main__":
    main()
