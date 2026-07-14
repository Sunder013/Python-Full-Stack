Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Copy,discard and clear
>>> a = {10,20,30,40,50}
>>> a.copy()
{50, 20, 40, 10, 30}
>>> b = a.copy()
>>> b
{50, 20, 40, 10, 30}
>>> a
{50, 20, 40, 10, 30}
>>> a.discard(40)
>>> a
{50, 20, 10, 30}
>>> a.clear()
>>> a
set()
>>> b = set()
>>> b
set()
>>> b.add(100)
>>> b
{100}
>>> b.add(200,300,400)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    b.add(200,300,400)
TypeError: set.add() takes exactly one argument (3 given)
>>> b.extend(200,300,400)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    b.extend(200,300,400)
AttributeError: 'set' object has no attribute 'extend'
>>> b.extend(200,300)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b.extend(200,300)
AttributeError: 'set' object has no attribute 'extend'
>>> b.add(200)
>>> b
{200, 100}
>>> b.append(300,400)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b.append(300,400)
AttributeError: 'set' object has no attribute 'append'
>>> b.append(300)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b.append(300)
AttributeError: 'set' object has no attribute 'append'
b
{200, 100}
