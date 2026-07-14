Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Intersction
>>> a = {1,2,3,4,5,6,7,8}
>>> b = {3,4,5,6,7)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> a = {1,2,3,4,5,6,7,8}
>>> b = {3,4,5,6,7}
>>> a.intersection(b)
{3, 4, 5, 6, 7}
>>> b.intersection(a)
{3, 4, 5, 6, 7}
