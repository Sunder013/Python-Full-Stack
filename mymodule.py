# modules

def greetings(name):
    print("welcome",name)

'''a = int(input("a value"))
b = int(input("b value"))
print("the sum is", a+b)'''

'''details = {"idnos":[10,20,30],
           "name":["shyam","sunder","srinivas"],
           "marks":[70,80,90]}'''


#4th auguest

# mymodule

'''if __name__ == "__main__":
    a = [10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("this pogram is run as script")
    else:
        print("this program is run as module")
dummy()'''


#math module
'''import math
print(math.pi)
print(math.pi*2)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,4))
print(math.log(2))
print(math.tan(45))
print(math.sin(60))
print(math.cos(30))
print(math.ceil(2.9))
print(math.ceil(5.9))
print(math.ceil(8))
print(math.floor(2.7))
print(math.acos(1))
print(math.factorial(5))'''

#from keyword
'''from math import pi,log,sqrt
print(pi)
print(log(9))
print(sqrt(2))'''

#system module
'''import sys
print(sys.path)
print(sys.version)'''


#os module
'''import os'''
'''print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.mkdir("aug5"))
print(os.listdir())
print(os.chdir("C:\\Users\\shyam\\AppData\\Local\\Programs\\Python\\Python314"))
print(os.listdir())'''


#ASCII
'''print(chr(67))

print(chr(65))

print(chr(90))

print(chr(93))

print(ord("a"))

print(ord("c"))

print(ord("z"))

print(ord(93))#error misplacement of module

print(chr("d"))#error'''


'''for i in range(97, 123):
    print(chr(i))'''
'''print(chr(i), end=",")'''

'''a = input("enter the input")
for i in a:
    print(i,"-",ord(i),end=",")
print("-",a)'''

