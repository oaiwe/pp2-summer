##Lab4//Python Modules
#Consider a module to be the same as a code library.
def greeting(name):
  print("Hello, " + name)
##
import mymodule

mymodule.greeting("Jonathan")
##When using a function from a module, use the syntax: module_name.function_name.
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
import mymodule

a = mymodule.person1["age"]
print(a)
##renaming module as mx
import mymodule as mx

a = mx.person1["age"]
print(a)
##example of a built-on func
import platform

x = platform.system()
print(x)
##listing all the func names
import platform

x = dir(platform)
print(x)
##importing parts from one mod to another
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
from mymodule import person1

print (person1["age"])
## exercises
import mymodule
###
import mymodule as mx
###
import mymodule
print(dir(mymodule))
###
from mymodule import person1