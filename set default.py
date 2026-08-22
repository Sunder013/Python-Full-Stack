Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #set default
>>> a = {"name":"shyam","city":"vijayawada"}
>>> a
{'name': 'shyam', 'city': 'vijayawada'}
>>> a.setdefault("mail","codegnan")
'codegnan'
>>> a
{'name': 'shyam', 'city': 'vijayawada', 'mail': 'codegnan'}
>>> a.setdefault("mail","shyam@codegnan")
'codegnan'
>>> a
{'name': 'shyam', 'city': 'vijayawada', 'mail': 'codegnan'}
>>> a.setdefault("email","shyam@codegnan.com")
'shyam@codegnan.com'
>>> a
{'name': 'shyam', 'city': 'vijayawada', 'mail': 'codegnan', 'email': 'shyam@codegnan.com'}
