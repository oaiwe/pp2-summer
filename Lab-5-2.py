##Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

text = input()
match = re.search( 'a(b{2,3})', text)
if match:
    print("1")
else:
    print("0")
