Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dictionaries
>>> #dict{}
>>> a = {"name":"shyam","year":2000,"month":05}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> a = {"name":"shyam","year":2000,"month":5}
>>> a
{'name': 'shyam', 'year': 2000, 'month': 5}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['name', 'year', 'month'])
>>> a.values()
dict_values(['shyam', 2000, 5])
>>> a.items()
dict_items([('name', 'shyam'), ('year', 2000), ('month', 5)])
>>> b = {"class","year"}
>>> type(b)
<class 'set'>
>>> b.values()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b.values()
AttributeError: 'set' object has no attribute 'values'
>>> b.keys()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b.keys()
AttributeError: 'set' object has no attribute 'keys'
