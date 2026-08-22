
>>> a = {"name":"shyam","city":"vja"}
>>> a
{'name': 'shyam', 'city': 'vja'}
>>> a.clear()
>>> a
{}
>>> b = {}
>>> b
{}
>>> b.update("name":"shyam","city:"vja"}
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> b.update("name":"shyam","city":"vja")
...          
SyntaxError: invalid syntax
>>> b
...          
{}
>>> b.update({"shyam","name"})
...          
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b.update({"shyam","name"})
ValueError: dictionary update sequence element #0 has length 5; 2 is required
>>> b.update({"shyam":"name"})
...          
>>> b
...          
{'shyam': 'name'}
a = int(input("a value"))
b = int(input("b value"))
c = input("choose the option add sub mul")
print(a+b)
print(a-b)
print(a*b)
