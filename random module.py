#random module
 #def - random module is used to generate random numbers in python, randint(single num) function is used and this function is defined in random module.
    #sample is attribute
'''import random
a = random.sample(range(10, 40), 10)
print(a)'''

#randint()
'''import random
a = random.randint(40,50)
print(a)'''

#choice()
'''import random
a = [10,20,30,40,50]
b = random.choice(a)
print(b)'''

#task - 1
'''import random
while True:
    input("enter the roll of dice")
    a = random.randint(1,6)
    print(a)
    options = (input("1.Yes"
                     "2.No" ))
    if options == "yes":
        continue
    elif options == "No":
        break
    else:
        print("invalid")'''

#calendar
'''import calendar
year = 2026
month = 9
print(calendar.month(year,month))'''

'''import calendar
year = 2026
print(calendar.calendar(year))'''

'''import calendar
year = 2027
print(calendar.calendar(year))'''

'''import calendar
a = int(input("enter the year"))
b = int(input("enter the month"))
print(calendar.month(a,b))'''

#date and time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a = datetime.datetime.now()
print(a)'''


#epoch time
import time
'''a = time.time() #time - module,time = attribute
print(a)#epoch time

b = time.localtime(a)
print(b)

print(f"{b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"time is {b.tm_hour}-{b.tm_min}-{b.tm_sec}")'''

#task - 2
'''import random
import time
input("enter the number")
a = random.sample(range(0,10), 2)
time.sleep(2)
print(a)'''


'''import random
import time
for i in range(1,11):
    a = random.randint(20,40)
    print(a)
    time.sleep(2)'''

'''import random
import time
for i in range(1,11):
    a = random.randint(20,40)
    print(a)
    time.sleep(2)'''



    





        

