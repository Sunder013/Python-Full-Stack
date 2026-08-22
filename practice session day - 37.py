#found greatest and second greatest

'''if :- [9,9,4,2,0,10,11,11]
if :- [9,2,3,0,5]'''

#task - 1

'''numbers = [9,9,4,2,0,10,11,11]                                                                      
greatest = numbers[0]
second = None
for num in numbers:
    if num > greatest:
        second = greatest
        greatest = num
    elif num != greatest and (second is None or num > second):
             second = num

    print("Greatest:", greatest)
    print("Second greatest:", second)'''



'''numbers = [-4,-3,-8,-2,-1,-7,-9]
greatest = numbers[0]
second = None
for num in numbers:
    if num > greatest:
        second = greatest
        greatest = num
    elif num != greatest and (second is None or num > second):
        second = num
    print("greatest:", greatest)
    print("Second greatest:", second)'''



numbers = [-6,-5,-4,-3,0,1,3,4,5]
greatest = numbers[0]
second = None
for num in numbers:
    if num > greatest:
        second = greatest
        greatest = num
    elif num != greatest and (second is None or num > second):
        second = num
    print("greatest:", greatest)
    print("Second greatest:", second)



