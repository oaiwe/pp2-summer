###PYTHON BOOLEANS
print(10 > 9)
print(10 == 9)
print(10 < 9)
###
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
###
print(bool("Hello"))
print(bool(15))
###
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
###
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
###
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
###
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
###I can create a func that returns a true value 
def myFunction() :
  return True

print(myFunction())
###
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
### It's checking whether the value is various data type or not
x = 200
print(isinstance(x, int))
### the same goes here but as False
x = 200
print(isinstance(x, str))
###
print(10 > 9)

#True
###
print(10 == 9)

#False
###
print(10 < 9)

#False
###
print(bool("abc"))

#True
###
print(bool(0))

#False
###PYTHON OPERATORS
print(10 + 5)
###
print(5+5)
#addition
print(5-5)
#substraction
print(5*5)
#multiplication
print(5/5)
#division
print(5%5)
#modulus
print(5**5)
#exponentiation
print(5//5)
#floor division
print(x:=3)
#print out "x=3"
x==y
x!=y
x>=y
x>y
x<=y
x<y
#operators and & or
x<5 and x<10
x<5 or x<4
#'not' reverse the result
not(x<5 and x<10)
###
#x is y
#returns True if both of them are the same
#x is not y
#returns True if both of them are different
##returns False otherwise
#membership operators:
#x in y
#returns True if x is present inside y
#x not in y 
#True if it's indeed not
#x<<2
#Shift left by pushing zeros in from the right and let the leftmost bits fall off
#x>>2
#Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print((6 + 3) - (6 + 3))
###
print(100 + 5 * 3)
#* > +
###
#parenthesis > exponentiation > unary plus/minus > multiplication/division ect. > add/sub > bitwise left/right > bitwise and/xor/or 
#> comparisons > logical NOT > and > or
###
print(5 + 4 - 7 + 3)
###
print(10 * 5)
###
print(10 / 2)
###
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
###
if 5 != 10:
  print("5 and 10 is not equal")
###
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
###
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
###PYTHON LISTS
mylist = ["apple", "banana", "cherry"]
###
thislist = ["apple", "banana", "cherry"]
print(thislist)
###
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#it allows duplicates
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
###
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
###
list1 = ["abc", 34, True, 40, "male"]
###
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
###
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
###
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
###
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
###
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
###
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
###
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
###
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
###
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
###
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
del thislist
###
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
###
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
###
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
###
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
###
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
###
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
###
newlist = [x for x in fruits if x != "apple"]
###
newlist = [x for x in fruits]
###
newlist = [x for x in range(10)]
print(newlist)
###
newlist = [x for x in range(10) if x < 5]
###
newlist = [x.upper() for x in fruits]
###
newlist = ['hello' for x in fruits]
###
newlist = [x if x != "banana" else "orange" for x in fruits]
###
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
###
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
###
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
###
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
###
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)
###
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
###
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
###
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
###
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
###
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
###
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
###
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
###
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
###
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
###
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
###
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
###
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
###
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
###
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
###
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
###PYTHON TUPLES
mytuple = ("apple", "banana", "cherry")
###
thistuple = ("apple", "banana", "cherry")
print(thistuple)
###
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
###
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
###
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
###
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
###
tuple1 = ("abc", 34, True, 40, "male")
###
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
###
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
###
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
###
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
###
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
###
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
###
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
###
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
###
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
###
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
###
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
###
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
###
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
###
#thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple) 
#this will raise an error because the tuple no longer exists
###
fruits = ("apple", "banana", "cherry")
###
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
###
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
###
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
###
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
###
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
###
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
###
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
###
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
###
fruits = ("apple", "banana", "cherry")
print(fruits[0])
###
fruits = ("apple", "banana", "cherry")
print(len(fruits))
###
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
###
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
###PYTHON SETS
myset = {"apple", "banana", "cherry"}
###
thisset = {"apple", "banana", "cherry"}
print(thisset)
###
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
###
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
###
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
###
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
###
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
###
set1 = {"abc", 34, True, 40, "male"}
###
myset = {"apple", "banana", "cherry"}
print(type(myset))
###
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
###
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
###
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
###
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
###
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
###
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
###
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
###
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
###
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
###
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
###
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
###
#thisset = {"apple", "banana", "cherry"}

#del thisset

#print(thisset)
###
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
###
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
### union - all elements from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
### 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
###
#The update() method inserts all items from one set into another.
#The update() changes the original set, and does not return a new set.
### The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
###
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
###
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
###
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
### The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
###
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
###
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
###The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
###
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
###
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
###
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
###

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
###
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
###
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
###
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
###PYTHON DICTIONARIES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
###Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
###
print(len(thisdict))
###
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
###
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
###
x = thisdict.get("model")
###
x = thisdict.keys()
###
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
###
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
###
for x in thisdict:
  print(x)
###
for x in thisdict:
  print(thisdict[x])
###
for x in thisdict.values():
  print(x)
###
for x in thisdict.keys():
  print(x)
###
for x, y in thisdict.items():
  print(x, y)
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
###
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
###
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
###
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
###
print(myfamily["child2"]["name"])
###
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
###
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
###

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
###
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
###

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
###
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
###PYTHON IF...ELSE
a = 33
b = 200
if b > a:
  print("b is greater than a")
###
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
###
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
###
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
###
if a > b: print("a is greater than b")
###
a = 2
b = 330
print("A") if a > b else print("B")
###
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
###
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
###
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
###
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
###
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
###
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
###
a = 33
b = 200

if b > a:
  pass
###

a = 50
b = 10
if a > b:
  print("Hello World")
###
a = 50
b = 10
if a != b:
  print("Hello World")
###
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
###
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
###
if a == b and c == b:
  print("Hello")
###
if a == b or c == b:
  print("Hello")
###
if 5 > 2:
    print("YES")
###
a = 2
b = 50
c = 2
if a == c or b == c:

  print("YES")
###PYTHIN WHILE LOOPS
i = 1
while i < 6:
  print(i)
  i += 1
###
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
###
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
###
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
###
i = 1
while i < 6:
  print(i)
  i += 1
###
i = 1
while i < 6:
  if i == 3:    
    break
  i += 1
###
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
###
i = 1
while i < 6:
  print(i)
  i += 1
else:

  print("i is no longer less than 6")
###PYTHON FOR LOOPS
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
###
for x in "banana":
  print(x)
###
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
###
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
###
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
###
for x in range(6):
  print(x)
###
for x in range(2, 6):
  print(x)
###
for x in range(2, 30, 3):
  print(x)
###
for x in range(6):
  print(x)
else:
  print("Finally finished!")
###
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
###
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
###
for x in [0, 1, 2]:
  pass
###
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
###
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":    
    continue
  print(x)
###
for x in range(6):  
  print(x)
###
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)