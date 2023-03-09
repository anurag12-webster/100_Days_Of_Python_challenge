# This code was written by @Anurag_Kanade on 9 march 2023
'''Write a program to find roots of a quadratic equation'''
import math


a = float(input())
b = float(input())
c = float(input())

# finding the discriminant of b square - 4ac
discriminant = b**2 - 4*a*c
if discriminant < 0:
    print("No real roots")
    # if no real valued exits 
    exit()
root1 = (-b + math.sqrt(discriminant)) / (2*a)             # x = (-b ± sqrt(b^2 - 4ac)) / 2a
root2 = (-b - math.sqrt(discriminant)) / (2*a)


print(root1, root2)
