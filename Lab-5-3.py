##Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

def lowercase_joined_underscore(text):
    pattern = r'[a-z]_[a-z]+'
    return re.findall(pattern, text)

def main():
    a = input("string: ")
    matches = lowercase_joined_underscore(a)
    if matches:
        print(matches)
    else:
        print("no sequences")

if __name__ == "__main__":
    main()
