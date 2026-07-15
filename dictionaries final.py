Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = {"idnos":[10,20,30],"names":["shyam","sunder","krishna"],"marks":[60,70,80]}
>>> a
{'idnos': [10, 20, 30], 'names': ['shyam', 'sunder', 'krishna'], 'marks': [60, 70, 80]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['shyam', 'sunder', 'krishna'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['shyam', 'sunder', 'krishna']), ('marks', [60, 70, 80])])
