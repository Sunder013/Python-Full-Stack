Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # difference
>>> a = {7,8,9,10,11,12,13}
>>> b = {8,9,10,11,12,13,14}
>>> a.difference(b)
{7}
>>> b.difference(a)
{14}
