# This code was written by @Anurag_Kanade on 7 march 2023
'''Day 6 coding Statement:  Write a program to find the Quadrants in which coordinates lie
Get the value of x and y coordinates as input from the user and check in which quadrant the point lies and print it.'''

# logic behind problem:
# if x is positive and y is positive -> first quadrant.
# if x is negative and y is positive -> second quadrant.
# if x is negative and y is negative -> third quadrant.
# if x is positive and y is negative -> fourth quadrant.
# else the point is at origin lies on x or y.

x = int(input('Enter the value of x:    '))
y = int(input('Enter the value of y:    '))

if x > 0 and y > 0:
    print('The point lies in First quadrant')
elif x < 0 and y >0:
    print('The point lies in Second quadrant')
elif x < 0 and y < 0:
    print('The point lies in Third quadrant')
elif x > 0 and y < 0:
    print('The point lies in Fourth quadrant')
else:
    print('Origin')

