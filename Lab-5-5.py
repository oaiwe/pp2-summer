##Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

def a_ending_in_b(text):
    pattern = r'a.*b'
    return bool(re.fullmatch(pattern, text))

def main():
    a = input("string: ")
    if a_ending_in_b(a):
        print("1")
    else:
        print("0")

if __name__ == "__main__":
    main()
