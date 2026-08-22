#functions
'''a = 10
b = 20
print("the sum is", a+b)
print("the diff is", a-b)
print("the product is", a*b)
a = 100
b = 200
print("the sum is difference is", a+b)
print("the diff is", a-b)
print("the product is", a*b)'''

'''a = 1000
b = 2000
print("the sum is", a+b)
print("the diff is", a-b)
print("the product is", a*b)'''

#functions:- not variables its arguements
'''def calculate(a,b):
    print("the sum is", a+b)
    print("the diff is", a-b)
    print("the product is", a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

# **,%,//
'''def calculate(a,b):
    print("the pow is", a**b)
    print("the intdiv is", a//b)
    print("the mod is", a%b)
calculate(10,20)
calculate(3,5)
calculate(4,6)'''

'''def add(a,b):
    print(a+b)
add(5,7)'''
'''while True:
    def add():
        a = int(input("enter the a value"))
        b = int(input("enter the b value"))
        print(a+b)
    add()'''
#recursive function without for loop by callig function it is called recursive function
'''def add():
        a = int(input("enter the a value"))
        b = int(input("enter the b value"))
        print(a+b)
        add()
add()'''

#usecase
'''def fullname():
    fname = input("first name")
    lname = input("last name")
    print((fname+" "+lname).title())
fullname()'''

#difference between print and return:
#print just shows the human user output in a console - display purpose
#return is a keyword and return is used to terminate the function and gives the value for the function - callback the function

#print vs return
'''def mul(a,b):
    print(a*b)
mul(4,5)'''

'''def mul(a,b):
    return (a*b)
print(mul(4,6))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,3)'''

#return will terminate the function and works only once only it display 1st function
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(4,6))'''

#problems on syntax
'''def cal():
        a = int(input("enter the a value"))
        b = int(input("enter the b value"))
        option=int(input(choose the option
                         1.add
                         2.sub
                         3.mul))
        if option == 1:
            print(a+b)
        elif option == 2:
            print(a-b)
        elif option == 3:
            print(a*b)
    cal()'''


'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
    while True:
        a = int(input("enter a value")
        b = int(input("enter b value")
        option = int(input('''choose the option
                                      1.add
                                      2.sub
                                      3.mul'''))
        if option == 1:
                    add()
        elif option == 2:
                sub()
        elif option == 3:
                mul()'''
        
    
    
    







