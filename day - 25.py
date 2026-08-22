#map() -> each object from a collection and







'''a = input("a value")
b = input("b value")
print(a+b)'''

'''a,b = input("enter the data").split(",")
print(a,b)'''

'''a,b = [x for x in input("enter the value").split(",")]
print(a,b)'''

'''a,b = map(str,input("enter the value").split(","))
print(a,b)'''

#for int
'''a = int(input("enter a value"))
b = int(input("enter b value"))
print(a+b)'''

'''a,b = int(input("enter the values").split(","))
print(a+b)#error - map is cumpolsary'''

'''a,b = [int(x) for x in (input("enter the value").split(","))]
print(a,b)'''

'''a,b = map(int,input("enter the values").split(","))
print(a,b)'''

#for list
'''a = list(map(int,input("values").split(",")))
print(a)
print(type(a))'''

'''a = tuple(map(int,input("values").split(",")))
print(a)
print(type(a))'''

'''a=set(map(int,input("values").split(",")))
print(a)
print(type(a))'''

#for dictionary
'''a=input("enter the key value")
b=dict(i.split(":") for i in a.split(","))
print(b)'''

#using eval
'''a = list(map(str,input("enter the value").split(",")))
print(a)
print(type(a))'''

'''a = list(map(eval,input("enter the value").split(",")))
print(a)
print(type(b))'''

#Difference between module,library and package.
 #Module-
  # A module in python is a single python file which consist of python code.
  # Examples of module includes (math.py, random.py, Mymodule.py)                   #import is a keyword
  # It contains functions, classes and variables.
 #Package -
  # One or more python modules is called package and (an, __init__.py)
  # Examples of packages include (requests, numpy, pandas)
 #Library
  #It consists both modules and packages.
  # Examples of libraries such as (numpy, pandas and matploitlib)
#Note:- Every python file is a module and import is a key word and every python file is saved internally with variable name as (__main__)
  
#Modules

  
  
















