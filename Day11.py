# getting the nth term from user
number = int(input())

# starting numbers in a fibonacci sequence
fibo= [0, 1]
if number<0:
    print('Sequence does not exist for negative value')
elif number == 0:
    print('Enter a positive value')
else:
# iterating over list starting from 2 2
    for i in range(2, number):
        previous = fibo[i-1]
        p_previous = fibo[i-2]
        value = previous + p_previous
        fibo.append(value)
    print(fibo)