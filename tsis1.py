print("Hello, World!")
###
if 5>2:
    print("Five is greater than two")
###
if 5>2:
    print("YES")
###
#comments in python are written with this character
#this is a comment
print("Hello, World!")
print("Hello, World!") #this is a comment
###
#print("Hello, World!")
print("Cheers, Mate!")
###
"""
this is a comment  
written in
more than just one line
"""
print("Hello, World!")
###
x=5
y="John"
print(x)
print(y)
###
x=4 #x is an int type
x="Sally" #x is now a str type
print(x)
###
x=str(3) #x will be '3'
y=int(3) #y will be 3
z=float(3) #z will be 3.0
###
x=5
y="John"
print(type(x))
print(type(y))
#we can get the type of a veriable this way
###
x="John"
#is the same as
x='John'
###
#A="Sally" will not overwrite a=4
###
#legal variable names:
#myvar = "John"
#my_var = "John"
#_my_var = "John"
#myVar = "John"
#MYVAR = "John"
#myvar2 = "John"
#illigal variable names:
#2myvar = "John"
#my-var = "John"
#my var = "John"
###
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
###
x = y = z = "Orange"
print(x)
print(y)
print(z)
###
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
###I should leave some space next to the words to have a readable phrase
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
###
x = 5
y = 10
print(x + y)
###
"""
x = 5
y = "John"
print(x + y) 
""" #will output error
###
x = 5
y = "John"
print(x, y)
###
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
###
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
###
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
### we have changed global variable inside a func
carname='Volvo'
print(carname)
###
x=50
print(x)
###
x=5
y=10
print(x + y)
###
x=5
y=10
z=x+y
print(z)
###
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)
###
x=y=z="Orange"
print(x, y, z)
###
x="wow"
def myfunc():
   global x
   x="fantastic"
   print(x)
myfunc()
###
x = 5
print(type(x))
#int
###
x = "Hello World"
print(type(x))
#str
###
x = 20.5
print(type(x))
#float
###
x = ["apple", "banana", "cherry"]
print(type(x))
#list
###
x = ("apple", "banana", "cherry")
print(type(x))
#tuple
###
x = {"name" : "John", "age" : 36}
print(type(x))
#dict
###
x = True
print(type(x))
#bool
###
x = 1    # int
y = 2.8  # float
z = 1j   # complex
###
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
###
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
###
#Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
###
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
###
import random

print(random.randrange(1, 10))
###
x=5
x=float(x)
print(x)
#x=5.0
x=5.5
x=int(x)
print(x)
###
x=5
x=complex(x)
print(x)
###
print("Hello")
print('Hello')
###
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
###
a = "Hello"
print(a)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#You can assign a multiline string to a variable by using three quotes
###
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#Or three single quotes
###
#Strings as Arrays

a = "Hello, World!"
print(a[1])
###
for x in "banana":
  print(x)
###
a = "Hello, World!"
print(len(a))
###
txt = "The best things in life are free!"
print("free" in txt)
###
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
###
txt = "The best things in life are free!"
print("expensive" not in txt)
###
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
###
b = "Hello, World!"
print(b[2:5])
###
b = "Hello, World!"
print(b[:5])
###
b = "Hello, World!"
print(b[2:])
###
b = "Hello, World!"
print(b[-5:-2])
#from the end of the string
###
a = "Hello, World!"
print(a.upper())
###
a = "Hello, World!"
print(a.lower())
###
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
###
a = "Hello, World!"
print(a.replace("H", "J"))
###
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
###
a = "Hello"
b = "World"
c = a + " " + b
print(c)
###
a = "Hello"
b = "World"
c = a + b
print(c)
###
age = 36
txt = f"My name is John, I am {age}"
print(txt)
###
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
###
txt = f"The price is {20 * 59} dollars"
print(txt)
###
#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
###
x = "Hello World"
print(len(x))
###
txt = "Hello World"
x = txt[0]
print(x)
###
txt = "Hello World"
x = txt[2:5]
print(x)
###
txt = " Hello World "
x = txt.strip()
print(x)
###
txt = "Hello World"
txt = txt.upper()
print(txt)
###
txt = "Hello World"
txt = txt.lower()
print(txt)
###
txt = "Hello World"
txt = txt.replace("H","J")
print(txt)
###
#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
