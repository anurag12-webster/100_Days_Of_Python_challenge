#  This code was written by @Anurag_Kanade on 10 march 2023
'''Day 10 coding Statement:  Write a program to find Factorial of a number'''

# change the value for a different result
num = int(input())
fact = 1

if num <=0 :
       print('Factorial of 0 is 1 ')

for i in range(1,num + 1):
       fact = fact*i
    
print("The factorial of",num,"is",fact)


