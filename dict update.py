Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict update
>>> a = {"year":2026,"month":"july","date":14}
>>> a
{'year': 2026, 'month': 'july', 'date': 14}
>>> a.update({"time":2})
>>> a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2}
>>> a.update({"day":"tuesday","place":"vijayawada")}
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> a.update({"day":"tuesday","place":"vijayawada"})
>>> a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2, 'day': 'tuesday', 'place': 'vijayawada'}
