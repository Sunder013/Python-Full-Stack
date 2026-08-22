#difference between break, continue and pass
#Break - break is used to terminate the entire loop.
#Continue - Continue is used to skip the current iteration and the rest of the code will continue.
#Pass - A pass is a null statement it does nothing but syntactically we need.

#break
'''a = 10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a = 20
while a>3:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(25):
    if i==19:
        break
    print(i)'''

'''a = "python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue

'''a = 30
while a>5:
    a = a-1
    if a==15:
     continue
    print(a)'''

'''a = 30
while a>5:
    a=a-1
    if a==15:
     continue
    print(a)'''

'''for i in range(25):
    if i==11:
     continue
    print(i)'''

'''a ="python"
for i in a:
    if i=="h":
     continue
    print(i)'''

#pass
'''a = 9
while a>3:
    print(a)
    a=a-1
    if a==7:
        pass'''

'''for i in range(25):
    if i == 20:
        pass
    print(i)'''


#Atm apllication
'''while True:
        Account = 100000
        password = 1234
        card =(input("insert the card"))
        if card == "c":
            print("welcome Shyam")
            password=int(input("enter the password:"))
            if password==password:
                option=int(input('''choose the option
                                    1.balance enquiry
                                    2.withdraw''')
                           if option== 1:
                               print("acc balance is",Account)
                           elif option== 2:
                               withdraw_money = int(input("enter the amount")
                                print(withdraw_money)
                                balance=Account-withdraw_money
                                print("remaining account balance is",balance)
            else:
                print("invalid option")
            else:
                print("incorrect password")
        else:
            print("invalid card")'''

    
        

