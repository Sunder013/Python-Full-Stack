#List comprehensions/Linear comprehension :
#Every list comprehension can be re written as a for loop but every for loop cannot be re written in list comprehension.
a = ["python","java","dsa"]
'''b = str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(), end=" ")'''

#syntax
#a = [exp for var in collection/range]
'''a = [i.upper() for i in a]
print(a)'''

#tasks:-
'''a = ["codegnan","course","python"]'''
'''b=[i.title() for i in a]
print(b)'''

'''b = [i.capitalize() for i in a]
print(b)'''

'''a = [1,3,4,5,6,7,8,12,13]'''
'''b =[i**2 for i in a]
print(b)'''
'''b = [i*i for i in a]
print(b)'''
'''b = [pow(i,2) for i in a]
print(b)'''

# if-usage in list 
'''a = [i for i in range(21) if i%2 == 0]
print(a)'''

'''a = [i for i in range(21) if i%2!=0]
print(a)'''

'''a = [i*i for i in range(21) if i%2==0]
print(a)'''

'''a = ["apple","banana","mango","dragon","kiwi","berry"]'''
'''b =  [i for i in a if "a" in i]
print(b)'''
'''b = [i for i in a if "a" not in i]
print(b)'''

#no elif usage

#if - else usage in list comprehension
'''a = [i**2 if i%2 == 0 else i*5 for i in range(16)]
print(a)'''

'''a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = [a[i]+b[i] for i in range(5)]
c = [a[i]+b[i] for i in range(len(a))]
print(c)'''

#task
#Attendence report
'''students = int(input("enter the total number of students"))
p=0
a=0
for i in range(1,students+1):
    attendence=input(f"students{i} (p/a)")
    if attendence=="p":
        p+=1
    elif attendence=="a":
          a+=1
print(".........attendence report.......")
print("total students",students)
print("total presenties",p)
print("total absenties",a)'''

    

        


    
