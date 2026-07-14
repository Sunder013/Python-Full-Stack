Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Symmetric difference update
>>> a = {11,12,13,14,15,16}
>>> b = {13,14,15,16,17,18}
>>> a.symmetric_update(b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.symmetric_update(b)
AttributeError: 'set' object has no attribute 'symmetric_update'
>>> a.symmetric_difference_update(b)
>>> a
{17, 18, 11, 12}
>>> b.symmetric_difference_update(a)
>>> b
{16, 11, 12, 13, 14, 15}
