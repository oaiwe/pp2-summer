##Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

text = input()
match = re.search('a.*b', text)
print(match)