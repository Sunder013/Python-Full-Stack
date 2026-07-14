Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #is disjoint
>>> a = {2,3,4,5,6,7}
>>> b = {6,7,8,9,}
>>> a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> a.isdisjoint(b)
False
>>> c = { 4,5,6,7,8,9}
>>> d = {50,60,70,80}
>>> c.isdisjoint(d)
True
