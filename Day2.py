# This code was written by @Anurag_Kanade on 3 march 2023

'''Day 2 coding Statement : Write a program to identify if the character is an alphabet or not.

Description:
Take an input character from user and check whether it is an alphabet or not.'''
E_char = input('Enter a Character: ')

# Here checking if entered character is an alphabet or not an alphabet.
if E_char>='A' and E_char<='Z':
    print('It is an Alphabet')
elif E_char>='a' and E_char<='z':
    print('It is an Alphabet')
else:
    print('It is not an Alphabet')