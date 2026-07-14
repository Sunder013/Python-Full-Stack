Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a = [2,4.5,"python",6+9j,True,False]
print(a)
[2, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=8.9
print(b)
8.9
type(b)
<class 'float'>
c=[8.9]
type(c)
<class 'list'>
d = ("python", 4.5)
type(d)
<class 'tuple'>

a = ["python","c","c++"]
a.append("java")
a
['python', 'c', 'c++', 'java']
a.append("html")
a.append
<built-in method append of list object at 0x000001B07200E700>
a
['python', 'c', 'c++', 'java', 'html']
a.append(["html","css"])
a
['python', 'c', 'c++', 'java', 'html', ['html', 'css']]

#extend
a = ["html","css","Java script"]
a.extend(["python", "sql"])
a
['html', 'css', 'Java script', 'python', 'sql']

#insert()
b = ["vja","hyd","vzg"]
b
['vja', 'hyd', 'vzg']
b.insert(1,"chennai")
b
['vja', 'chennai', 'hyd', 'vzg']
b.insert(2,"coimbatore")
b
['vja', 'chennai', 'coimbatore', 'hyd', 'vzg']

#Index
a = ["apple","grapes","banana"]
a.index
<built-in method index of list object at 0x000001B0723F7E40>
a.index("grapes)
        
SyntaxError: unterminated string literal (detected at line 1)
a.index("grapes")
        
1
a.copy()
        
['apple', 'grapes', 'banana']
b = a.copy()
        
c = b.copy()
        
c
        
['apple', 'grapes', 'banana']
b
        
['apple', 'grapes', 'banana']
a.count("apple)
        
SyntaxError: unterminated string literal (detected at line 1)
a.count("apple")
        
1
a.count("grapes")
        
1
b.count("banana")
        
1
c.count("grapes")
        
1
d = "apple"
        
d
        
'apple'
d = "apple"
        
len(d)
        
5
e = ["banana"]
        
len(e)
        
1

#sorting
        
a = ["mango","kiwi","berry","apple"]
        
a.sort()
        
a
        
['apple', 'berry', 'kiwi', 'mango']
b = [9,3,4,7,8,45,67,32,45,12,89,99]
        
b
        
[9, 3, 4, 7, 8, 45, 67, 32, 45, 12, 89, 99]
b.sort()
        
b
        
[3, 4, 7, 8, 9, 12, 32, 45, 45, 67, 89, 99]

#Reverse
        
a = ["ds","ai","ml"]
        
a
        
['ds', 'ai', 'ml']
a.reverse()
        
a
        
['ml', 'ai', 'ds']
b = [9,0,8,7,6,5,4,3,2,1]
        
b.reverse()
        
b
        
[1, 2, 3, 4, 5, 6, 7, 8, 0, 9]

#Pop Operation
        
a = ["black","white","pink","green"]
        
a
        
['black', 'white', 'pink', 'green']
a.pop()
        
'green'
a
        
['black', 'white', 'pink']
a.remove("pink")
        
a
        
['black', 'white']
a.pop(1)
        
'white'
a
        
['black']
a.remove(0)
        
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.remove(0)
ValueError: list.remove(x): x not in list
a
        
['black']
a.push("white")
        
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.push("white")
AttributeError: 'list' object has no attribute 'push'
a
        
['black']
a.append("white")
        
a
        
['black', 'white']
a.append("pink)
         
SyntaxError: unterminated string literal (detected at line 1)
a.append("pink")
         
a
         
['black', 'white', 'pink']
a.append("green")
         
a
         
['black', 'white', 'pink', 'green']

#clear
         
a = ["ap","ts","ks","tn"]
         
a
         
['ap', 'ts', 'ks', 'tn']
a.clear()
         
a
         
[]
a.append("ap")
         
a
         
['ap']
a.extend("ts","ks","tn")
         
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.extend("ts","ks","tn")
TypeError: list.extend() takes exactly one argument (3 given)
b.extend("ts","ks","tn")
         
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    b.extend("ts","ks","tn")
TypeError: list.extend() takes exactly one argument (3 given)
a
         
['ap']
a.extend(["ts","ks"])
         
a
         
['ap', 'ts', 'ks']
a.append(["tn"])
         
a
         
['ap', 'ts', 'ks', ['tn']]
# Tuple
         
a = ("tuple",4.5,10,"chennai")
         
type(a)
         
<class 'tuple'>
a.tuple()
         
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.tuple()
AttributeError: 'tuple' object has no attribute 'tuple'
a()
         
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a()
TypeError: 'tuple' object is not callable
type(a)
         
<class 'tuple'>
['ap', 'ts', 'ks', ['tn']]# Tuple
         
['ap', 'ts', 'ks', ['tn']]
a
         
('tuple', 4.5, 10, 'chennai')
type(a)
         
<class 'tuple'>
a = (4,5.6,"python",8+9j,True,False)
         
a
         
(4, 5.6, 'python', (8+9j), True, False)
print(a)
         
(4, 5.6, 'python', (8+9j), True, False)
type(a)
         
<class 'tuple'>
a.index(8+9j)
         
3
a.index(false)
         
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a.index(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
a.index(False)
         
5
a.count("python")
         
1
a.count(python)
         
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    a.count(python)
NameError: name 'python' is not defined
a.count(True)
         
1
a.count(8+9j)
         
1

#Sets
         
a = {4.5,7,"Shyam",5=9j,True,False}
         
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a = {4.5,7,"Shyam",5+9j,True,False}
         
a
         
{False, True, (5+9j), 4.5, 'Shyam', 7}
>>> type(a)
...          
<class 'set'>
>>> b = {7,9,5,4,2,1,6}
...          
>>> print(b)
...          
{1, 2, 4, 5, 6, 7, 9}
>>> type(b)
...          
<class 'set'>
>>> 
>>> #add
...          
>>> a = {4,5,6,7,8,9}
...          
>>> a
...          
{4, 5, 6, 7, 8, 9}
>>> a.add()
...          
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    a.add()
TypeError: set.add() takes exactly one argument (0 given)
>>> a = {5,6,7,8,9,10,11}
...          
>>> b = {7,8,9,10}
...          
>>> a.issuperset(b)
...          
True
>>> b.issuperset(a)
...          
False
>>> a = {4,5,6,7,8,9}
...          
>>> b = {7,8,9}
...          
>>> a.issubset(b)
...          
False
>>> b.issubset(a)
...          
True
