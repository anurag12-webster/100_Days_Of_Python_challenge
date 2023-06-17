Str1 = input('Enter a string:')

Sum = 0

for i in Str1:

    if ord(i) >= 48 and ord(i) <= 57:

        Sum = Sum + int(i)

print('Sum is: ' + str(Sum))