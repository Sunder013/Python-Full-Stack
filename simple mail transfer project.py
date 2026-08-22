#email automation
#otp generation
import random
import math
import smtplib# simple mail tarnsfer protocol

digits = "0123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+ "is your otp"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("shyam9100197195@gmail.com","iwko nrok rugy rxhc")
user="shyam9100197195@gmail.com"
email=input("enter the mail_id")
s.sendmail(user, email, msg)

while True:
    a=input("validate the otp")
    if a==OTP:
        print("Account successfully verified")
    else:
        print("Invalid otp")
