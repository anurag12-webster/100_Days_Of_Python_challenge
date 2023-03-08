# This code was written by @Anurag_Kanade on 8 march 2023
'''Write a program to find Number of days in a given month of a given year
'''
Year = int(input('Enter year: '))
Month = int(input('Enter month: '))

if Year % 4 != 0:
    leap = False
elif Year % 100 == 0 and Year % 400 != 0:
    leap = False
else:
    leap = True

if Month in [1,3,5,7,8,10,12]:
    daysinmonth = 31
elif Month in [4,6,9,11]:
    daysinmonth = 30
else:
    if leap:
        daysinmonth = 29
    else:
        daysinmonth = 28
print(daysinmonth)
