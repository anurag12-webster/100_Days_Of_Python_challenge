Str1 = input('Enter a string: ')

Str1 = Str1[0:1].upper() + Str1[1:len(Str1)-1] + Str1[len(Str1)-1:len(Str1)].upper()

print(Str1)