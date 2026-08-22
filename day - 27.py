#..........Excption handling............

 #try-> instructions from which we are expecting the exceptions.
 #except - > exceptions are raised in try block it will be handle by this block.
 #else - > no exceptions(it was optional)
 #finally - > always it will display.

'''while True:
    try:
        a = int(input("a value"))
        b = int(input("b value"))
        c = a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print(".....program ends here.....")'''


#File handling
 #write()
'''a = open("shyam.txt","w")
b = a.write("python full stack")
a.close()'''

'''a = open("shyam.txt","w")
a.write("codegnan it solutions")
a.close()'''

#append()
'''a = open("shyam.txt","a")
a.write("sunder")
a.close()'''

'''a = open("shyam.txt","a")
b = a.write("\tsunder")
a.close()'''

# task - 1
'''a = open("shyam.txt","w")
b = a.write(input("enter the data"))
a.close()'''

'''a = open("shyam.txt","w")
b = input("enter the data")
a.write(b)
a.close()'''

# task - 2
'''a = open("shyam.txt","w")
b = a.write("codegnan\tteaches\tvarious\tcourses\tlike\tpython,\tjava,\tcloud")
a.close()'''

'''a = open("shyam.txt","w")
b = input("enter the data")
a.write(b)
a.close()'''

#readlines()
a = open("shyam.txt")
#print(a.read()) it will display entire content
#print(a.readline()) it wiil display the first line of the data
#print(a.readlines()) it will display in list with \n
#print(a.read(7)) it will display the first 7 letters of the data in the line as no.of characters

#writelines() - > 
'''a = open("sunder.txt","w")
b = ["shyam","sunder","srinivas","janardhan"]
a.writelines(b)
a.close()'''

#task -1
'''a = open("sunder.txt","w")
a.writelines("shyam\nsunder\nsrinivas\njanardhan\n")
a.close()'''


'''a = open("sunder.txt","w")
b = ["shyam","sunder","srinivas","janardhan"]
a.writelines("\n".join(b))
a.close()'''

#fileaccess()
'''a = open("F:\\aug 5th\\random module.py")
print(a.read())'''

'''a = open("symmetric difference update.py")
print(a.read())'''



