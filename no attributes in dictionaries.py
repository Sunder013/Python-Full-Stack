Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = {"colour":"black","food":"biryani"}
>>> a
{'colour': 'black', 'food': 'biryani'}
>>> a.copy()
{'colour': 'black', 'food': 'biryani'}
>>> b = a.copy()
>>> b
{'colour': 'black', 'food': 'biryani'}
>>> len(a)
2
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
>>> a = {"name":"shyam","city":"vijayawada"}
>>> a
{'name': 'shyam', 'city': 'vijayawada'}
>>> a = {"name":"shyam","city":"vijayawada","name":"shyam"}
>>> a
{'name': 'shyam', 'city': 'vijayawada'}
>>> a = {"name":"shyam","city":"vja","name":"sunder"}
>>> a
{'name': 'sunder', 'city': 'vja'}
>>> a = {"name1":"shyam","city":"vja","name2":"sunder"}
>>> a
{'name1': 'shyam', 'city': 'vja', 'name2': 'sunder'}
>>> a.count("name1")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.count("name1")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("name2")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.index("name2")
AttributeError: 'dict' object has no attribute 'index'
