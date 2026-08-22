#OOP Concept - Object Oriendted Programming System

#Programming is nothing but a giving a set of instructions to the computer, in order to solve a problem.

#When we take an example then we give an input of data, then tells the computer take this data as a input and do the action and produce the output.

#These type of operations we already learned on the Data Analysis and the numpy and pandas, matplotlib.

#so in order to continue to proceed with the Object Oriented Programming....


#Action - 1

#data report for students

'''name1 = "Riya"
marks1 = [70,80,90]

name2 = "Arjun"
marks2 = [60,70,80]


def average_marks(marks):
    return sum(marks) / len(marks)
def print_report(name, marks):
    avg = average_marks(marks)
    print(f"Student: {name}")
    print(f"Marks:  {marks}")
    print(f"Average: {avg:.2f}")

while True:
    student = input("enter the students name")
    if student == "Riya":
        print_report(name1, marks1)
    elif student == "Arjun":
        print_report(name2, marks2)
    elif student == "exit":
        print("Programme stops here")
        break
    else:
        print("Student not found.")

print_report(name1, marks1)
print_report(name2, marks2)'''


#Now if you have a limited set of data reports of students then its easy to maintain the report cards of the students.

#What if you have a total 100's of students data...its a bit complicated to maintain and run the data.

#what if you request for (name1, marks2) - python will happily proceeds with your input by giving 1st student name with 2nd student marks, so with high volume of the data its a bit complicated to maintain data effeciently there will be a possibility of data clumsy.

#so thats where OOPS concept was useful to overcome the data clumsiness.

#instead of keeping the students data and function that works on that data as separate, scattered pieces - "BUNDLED THEM TOGETHER INTO ONE - SELF - CONTAINED UNIT".

#Each student becomes one package that who carries own names, marks, roll number etc....

#The core point of procedural code(data and functions disconnected, causing mixups as things scale).

#Syntax of the class - Class - keyword, class.name(): - Class definition
#                                            |
#                                            ^
                                        # class body - methods, ariables conditions statements, looping sts, adv python func , another class also created in these body.


'''# when obj was creaated then only memory was created - object was knows as physical entity - in class we can create 'n' no. of objects. - (data, function).
                        |
                        ^
                #The process of creating the object is known as the instantiation - syntax - obj name = class name()

                # if we want to use the specific class then we use the object name in the class to use its variables and functions.

                #syntax :- object name.method()
                #          object name.variable


            # keyword - class a(): - definition
            #                 |
            #                 ^
                         #class name#
            # b = a() - obj creation
               |
           # object#


#self is used to call methods or variables in our current class.
# can create multiple objects.'''





# Class Work

#OOPS
#Syntax
'''class classname():
    #attributes
    name = "Shyam"
    age = 25
    place = "vja"
    def fname(method_name):
        print("statements......")
a=classname()
print(dir(a))
a.fname()'''

#Class declaration
'''class details():
    name = "Shyam"
    age = 25
    place = "vja"
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''


#Object Instantiation

'''class Details():
    def data(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("shyam",24,"vja")
a.display()
b = Details()
b.data("Sunder",25,"vja")
b.display()
c = Details()
c.data("Srinivas",48,"vja")
c.display()'''


#Object initiation
'''class Data():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
a = Data("Shyam",23,"vja")
print(dir(a))
a.display()
b = Data("Sunder",24,"vja")
b.display()
c = Data("Srinu",40,"vja")
c.display()'''

#Task - 1
'''class Data():
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
a = Data(input("enter the name"),int(input("enter the age")),input("enter the place"))
print(dir(a))
a.display()'''

'''class Data():
    def __init__ (self):
        self.name = input("name")
        self.age = int(input("age"))
        self.place = input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Data()
print(dir(a))
a.display()'''
        

#Diff b/w _ and __

 #Def :- When user wants to create a variable in python by using double leading underscore, our python interpreter treats it as a special variable to avoid name conflicts with methods and inner classes.
'''class Employee1():
    def __init__(self):
        self.name="Shyam"
        self._mailid="shyam@gmail.com"
        self.__salary=25000#private variable
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee1__salary)

class Employee2():
    def __init__(self):
        self.name="sunder"
        self._mailid="Sunder@gmail.com"
        self.__salary=30000#private variable
a=Employee2()
print(dir(a))####
print(a.name)
print(a._mailid)
print(a._Employee2__salary)'''

#polymorphism
'''a=4;b=8
print(a.__add__(b))
print(a.__sub__(b))
print(a.__sub__(2))
print(a.__mul__(3))
print(a.__pow__(2))
#print(a.__div__(4)) gives error because it isnt available there
print(a.__eq__(4))#equal_to
print(a.__le__(8))#lessthan_or_equal_to
print(a.__ge__(10))#greater_than_or_equal_to
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(a.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
print(a.__add__(" "+b))
a="python";b="fullstack"
print(a.__add__(" "+b))
print(a.__add__(" "+b).title())
a=6+3j;b=8+9j
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(2))
print(a.__getstate__())
a="True";b="False"
print(a.__add__(b))'''


#operator overriding

'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(6)
y=B(4)
#x=6
#y=4
print(x+y)'''

#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("the programme ends here")
a=new()
a.sum()
a.sum(3,6,8)
a.sum(4,5)'''

#method overriding
'''class Animal():
    def speak(self):
        print("animal can make sound")
class Dog():
    def speak(self):
        print("dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''


'''class Vehicle():
    def sound(self):
        print("vehicles make sound")
class Bike():
    def sound(self):
        print("makes sound")
class Car():
    def sound(self):
        print("makes engine sound")
a=Vehicle()
b=Bike()
c=Car()
a.sound()
b.sound()
c.sound()'''
            


'''class car():
    def vehicle(self):
        print("thar")
    class bike():
        def vehicle(self):
            print("pulsar")
a=car()
b=bike()
a.vehicle()
b.vehicle()'''



#Inheritance
 #single - inheritence - who has one parent and n no. of child classes which has more than 2 or more.
    # we can access parent class via child class but we didnt access child class via parent class.

'''class RBI():
    cash = 100000
    def available_cash(cls):
        print("avalilable cash is", cls.cash)
        #print("available cash is", RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash = 50000
    def available_new_cash(cls):
        print("available_new_cash is", cls.cash+cls.cash)
        #print("available_new_cash is", cls.cash+RBI.cash)
a=HDFC()
b=SBI()
a.available_cash()
a.available_new_cash'''



'''class RBI():
    cash = 100000
    def available_cash(cls):
        #print("avalilable cash is", cls.cash)
        print("available cash is", RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash = 50000
    def available_new_cash(cls):
        #print("available_new_cash is", cls.cash+cls.cash)
        print("available_new_cash is", cls.cash+RBI.cash)
a=HDFC()
b=SBI()
a.available_cash()
a.available_new_cash'''


#Multiple_inheritence
    # 2 parents 1 child

'''class Father():
    def height(cls):
        print("father height is 5.8ft")
class Mother():
    def weight(cls):
        print("mother weight is 68kgs")
class Child(Father, Mother):
    def date_of_birth(cls):
        print("child date of birth was 28-05-2000")
a=Father()
b=Mother()
c=Child()
a.height()
b.weight()
c.date_of_birth()'''


# type - 2

'''class Father():
    def height(cls):
        print("father height is 5.8ft")
class Mother():
    def weight(cls):
        print("mother weight is 68kgs")
class Child(Father, Mother):
    def date_of_birth(cls):
        print("child date of birth was 28-05-2000")
c=Child()
c.height()
c.weight()
c.date_of_birth()'''


#Multilevel_inheritence - inheriting the previous class into this class.

'''class grand_parent():
    def land(cls):
        print("the land is 1 acre")
class parent():
    def house(grand_parent):
        print("the house was 100 sq.ft")
class child(parent):
    def bike(cls):
        print("the bike is Pulsar")
a=child()
a.land()
a.house()
a.bike()'''


'''class grand_parent():
    def land(cls):
        print("the land is 1 acre")
class parent(grand_parent):
    def house(cls):
        print("the house was 100 sq.ft")
class child(parent):
    def bike(cls):
        print("the bike is Pulsar")
a=grand_parent()
b=parent()
c=child()
a.land()
b.house()
c.bike()'''


#Hierarchical - Inheritance
 # def - hierarchical inheritance is one parent calss is inherited by multiple child classes.


'''class employee():
    def company(cls):
        print("the company name was infotech")
class trainer(employee):
    def teaching(cls):
        print("teaching teach the code")
class developer(employee):
    def developing(cls):
        print("developing the coding")
a=trainer()
a.company()
a.teaching()
b=developer()
b.developing()
b.developing()'''


#Hybrid inheritence - means combining one or more than one type of inheritence
 # ex - multilevel and hierarchical.
'''class trainer():
     def teaching(self):
         print("teaching the code")
class student():
    def learning(self):
        print("learning the code")
class person(trainer, student):
    def details(self):
        print("teaching and learning")
class program_manager(trainer, student):
    def manage(self):
        print("managing the records")
a=person()
a.details()
a.teaching()
b=program_manager()
b.teaching()
b.learning()'''


#hence completed all Inheritence topics.


#Encapsulation
 #Def :- Encapsulation means keeping data and the methods that operate on that data together inside a class, while controlling how that data is accessed or modified.
        # combining multiple units into single unit is known as the encapsulation.
        # 3 types
        # 1. protected
        # 2. private
        # 3. public

'''class bank_account:
    def __init__(self, balance):
        self.balance = balance
account = bank_account(10000)
#print(account.balance)
account.balance = -5000'''
'''print(account.balance)# we dont want to directly manipulate the internal account balance.
#thats where we use encapsulation.
#bank should maintain and manipulate the internal balance.
#we want the class itself to control the bank balance.
# we use __balance: - to protect the data.'''


'''class bank_account:
    def __init__(self, balance):
        self.__balance = balance# __double underscore indicates a private attribute.
account = bank_account(10000)
print(account.__balance)#gives error because balance was intended to be accessed through the class's controlled methods.'''

#programme - 1 - protected balance
'''class bank_account:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
account = bank_account(10000)
print(account.get_balance())'''
        

#programme - 2
'''class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
Employee.__salary = 50000
print(Employee.__salary)'''


#programme - 3
'''class employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
e = employee("Shyam", 35000)
#print(e.get_salary())
e = employee("shyam", 40000)
print(e.set_salary())'''



#public data
'''class A():
    public_data = 100
    def method_1(self):
        print(self.public_data)
class B(A):
    def method_2(self):
        print(self.public_data)
obj1=B()
obj1.method_1()
obj1.method_2()'''


'''class A():
    public_data = 100
    def method_1(self):
        print(self.public_data)
class B(A):
    def method_2(self):
        print(self.public_data)
obj1=A()
obj1=B()
#obj1.method_1()
obj1.method_2()'''

#Protected_data()
'''class A():
    _protected_data = 10
    def method1(self):
        print(self._protected_data)
class B(A):
    def method2(self):
        print(self._protected_data)
obj1=B()
obj1.method1()
obj1.method2()
print(obj1._protected_data)'''

#__Private_data()
'''class A():
    __private_data = "shyam"
    def method1(self):
        print(self.__private_data)      #recheck 
class B():
    def method2(self):
        print(self._A__private_data)
obj1 = A()
obj1.method1()'''


'''class A():
    __private_data = "shyam"
    def method1(self):
        print(self.__private_data)      #recheck 
class B(A):
    def method2(self):
        print(self._A__private_data)
obj1 = B()
obj1.method1()
obj1.method2()'''


#super()

'''class parent():# super class
    def __init__(self,name):
        self.name = name
        print("parent constructor")
class child(parent):#sub class
    def __init__(self,name,age):
        self.age = age
        #super().__init__(name) - by not giving the super keyword we cant able to call the parent class attribute to the subclass with the help of super keyworld only then we can able to call super class attribute to the sub class attribute.
        print("child constructor")
a=child("shyam", 25)
print(a.age)
print(a.name)'''



'''class parent():# super class
    def __init__(self,name):
        self.name = name
        print("parent constructor")
class child(parent):#sub class
    def __init__(self,name,age):
        self.age = age
        super().__init__(name)
        print("child constructor")
a=child("shyam", 25)
print(a.age)
print(a.name)'''



#Abstraction
 #def :- hiding unnecessary information from user is called abstraction.
 # in abstraction we have 2 types abstract class and abstract method.
 # abstract class - one or more abstract methods is called abstract class.
 # abstract method - the method is declared without implementation is called abstract method.


#programme - 1
'''class A():
     def method1(self):
         pass
obj1 = A()
obj1.method1()'''

'''class A():
    def method1(self):
        print("data")
obj1 = A()
obj1.method1()'''

'''from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("data science")
obj1 = A()
obj1.method1()'''

'''from abc import ABC, abstractmethod
class A():
    @abstractmethod     #without inherit the ABC class
    def method1(self):
        print("data science")
obj1 = A()
obj1.method1()'''


'''from abc import ABC, abstractmethod
class A():
    def method1(self):
        print("python course")
obj1 = A()
obj1.method1()'''

'''from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("data science")
obj1 = A()
obj1.method1()'''



'''from abc import ABC, abstractmethod
class A():
    def method1(self):
        pass
    def method2(self):
        print("python full stack")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("data structures")
    def method3 (self):
        print("java full stack")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''




