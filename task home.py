# split bill task

#normal form
'''n = 10
a = 20000
b = (a / n)
print("each person should pay:", b)'''

#with "f string
'''n = 10
a = 20000
b = a / n
print(f"total number of persons:{n}")
print(f"total amount:{a}")
print(f"total bill:{b}")'''

#with functions
'''def cal():
    a = int(input("enter the total number of persons"))
    b = int(input("enter the total bill amount"))
    c = b / a
    print(f"each person should pay:",{c})
cal()'''

'''while True:
    def cal():
        a = int(input("enter the total number of persons"))
        b = int(input("enter the total bill amount"))
        c = b / a
        print(f"each person should pay:",{c})
    cal()'''

'''while True:
    def cal():
        a = int(input("enter the total numbers"))           #after return it ends function immediately so after return the code should be intended.
        b = int(input("enter the total bill amount"))       #it should be outside the function so it will be intended.
        c = b / a
        return c

    bill = cal()
        
    print(f"each person should pay: {bill}")'''

#28th july

'''def splitbill():
    a = int(input("enter the no.of friends"))
    b = int(input("enter the total bill amount"))
    print(f"per head bill is {b//a}")
    print("per head bill is {}".format(b//a))
splitbill()'''

#Keyword and positional arguements:

'''def details(id,name,mailid):
    id = 10
    name = "shyam"
    mailid = "shyam@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id="10",name="shyam",mailid="shyam@gmail.com")
details(id="20",name="sunder",mailid="sunder@gmail.com")
details(id="30",name="srinivas",mailid="srinivas@gmail.com")
details(40,"janardhan","janardhan@gmail.com")
details("sanvi","sanvi@gmail.com",50)
details(name="vijay",id=60,mailid="vijay@gmail.com")'''

# default arguements
'''def groceries(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
groceries("rice",1500)'''

'''def groceries(item = "sugar",price = 100):
    print("item is %s" %item)
    print("price is %.2f" %price)
groceries()'''

'''def groceries(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
groceries("dhal")'''

'''def groceries(item="ghee",price):
    print("item is %s" %item)
    print("price is %.2f" %price)
groceries(500)'''

#task - 1
'''def bakery(cake,price,quantity):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %.2f" %quantity)
bakery("vanilla",750,2.5)'''

'''def bakery(cake="vanilla",price=750,quantity=2.5):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %.2f" %quantity)
bakery()'''

'''def bakery(cake,price=750,quantity=3.5):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %.2f" &quantity)
bakery("butterscotch")'''

#star arguements: used to unpack elements and also used to pass values to multiple arguements aswell
'''a=[10,20,30,40,50]
print(a)
print(*a)'''

'''a=(10,20,30,40,50)
print(a)
print(*a)'''

'''a={10,20,30,40,50}
print(a)
print(*a)'''

'''a = {"year":2026,"month":"july"}        #in dictionary it will show only the key values
print(a)
print(*a)'''

'''a,b,c=2,4,6
print(a)
print(b)
print(c)'''

'''a,*b,c=2,4,6,7,8,9
print(a)
print(*b)
print(c)'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''







    




    
            
    
