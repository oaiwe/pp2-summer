#RegEx can be used to check if a string contains the specified search pattern.
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
#to see if it starts with "The" and ends with "Spain":
#findall	Returns a list containing all matches
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#search	Returns a Match object if there is a match anywhere in the string
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
#split	Returns a list where the string has been split at each match
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#sub	Replaces one or many matches with a string
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#match object
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match
