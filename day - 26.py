#regex(regular_expressions)
 #regular expresions are powerful tool(module) embedded in python which is mainly used to find a pattern within a given string or statements or files and we mainly use it for text manipulation.
'''a = "codegnan is in vijayawada"
print(a)'''

'''a = "codegnan\nis\tin\nvijayawada"
print(a)'''

#rstring
'''a = r"codegnan\nis\tin\nvijayawada"
print(a)'''

#compile(), search(), findall(), split(), sub
# sequence characters
'''\w -> it matches alphanumeric
\W -> it matches non alpha numeric
\d -> it matches any digit
\D -> it matches non digit
\s -> it represents white spaces
\S -> it represents non-white spaces'''

#concept starts here....
#compile()
import re
'''a = "map maths mat cat code cash money cup cap monkey"
b = re.compile(r"m\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)

b = re.search(r"m\w+", a)
print(b)

#findall()
c = re.findall(r"m\w+",a)
print(*c) # to unpack and print * given

#split() - to separate everything
d = re.split(r"m",a)
print(d)

e = re.split(r"\S",a)
print(e)

#sub()
f = re.sub(r"m","a",a)
print(f)'''

#digits()
'''import re
g = "year 2026 month 08 day 06"
f = re.findall(r"\d+",g) #if not put + then it will print every character separately
print(f)

e = re.findall(r"\D+",g)
print(e)'''

#error handling()
 # syntax_error --> it will happen while compiling...compilation_error in the script no interpreter was inolved
 # run_time error -> it will happens when we excute the code during the excution.
 # logical_error --> it will happens in logics which can get error in logics (it can't be visible)
#syntax error
'''for i in range(20):
     print(i)'''
#run_time error
'''a = int(input("a value"))
b = int(input(" b value"))
print(a//b)''' #10//0zero division error

#logical_error
'''a = 10
b = 20
print(a-b)''' #cant be visible






