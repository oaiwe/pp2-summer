##Python Iterators
##All containers are iterable
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
###Strings are iterable
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
###u can loop through an iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
###u can loop thrugh a word iterating each letter
mystr = "banana"

for x in mystr:
  print(x)
###Iterating through forever
class MyNumbers: #create a class
  def __iter__(self): #create a starting point of iteration
    self.a = 1
    return self

  def __next__(self): #create a func that continues it
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers() #declare ur class
myiter = iter(myclass) #declare iterator

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
###Stopping the iteration until some condition is happened
class MyNumbers: 
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
###Python Scope
##variable X is created inside myfunc so it only can be used inside one (local scope)
def myfunc():
  x = 300
  print(x)

myfunc()
##though X is created inside myfunc it is usable inside any func that is nested inside the 1st one
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
##X now is created as a global variable so it doesn't matter where do u use it
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
##X-es are different here and will be printed out as local (1st) and global (2nd)
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
##variable stuck inside a local func can be called out as a global one
def myfunc():
  global x
  x = 300

myfunc()

print(x)
###we're changing global X inside func
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
print(myfunc1())
###Python Dates
##retruning actual datetime 
import datetime

x = datetime.datetime.now()
print(x)
##outpuying exact data from datetime
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
###Python Math
##finding the lowest and highest valuables
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
##abs returns absolute value of a number
x = abs(-7.25)

print(x)
##4 to the power of 3
x = pow(4, 3)

print(x)
##importing 'math' module so u can use math funcs
import math

x = math.sqrt(64)

print(x)
##ceil as the nearest wich is bigger and floor is nearest wich is smaller
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1
##
import math

x = math.pi

print(x)
###Python JSON
#JSON is a syntax for storing and exchanging data.
#JSON is text, written with JavaScript object notation.
##From JSON to Python
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])
##from Python to JSON
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)
##importing all the leagl data inside container into JSON
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
##making indents so its easier to read 
json.dumps(x, indent=4)
##