#  This code was written by @Anurag_Kanade on 15 march 2023
'''Day 12 coding Statement:  Write a program to find Sum of n natural numbers.'''

n = int(input("Enter the value of n: "))
sum = 0

for i in range(1, n+1):
    sum += i

print("Sum of first", n, "natural numbers is:", sum)
