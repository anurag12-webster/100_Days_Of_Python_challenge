# This code was written by @Anurag_Kanade on 2 march 2023

'''Day 1 coding Statement: Write a program to identify if the character is a vowel or consonant.
Description of the program: 
Take an input character from the user and check whether the given input is a vowel or consonant.
Input
A
Output
Vowel'''


vowel = ['A','E','I','O','U','a','e','i','o','u']
conso = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z','b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


isVowel = input('Enter a Character: ')

# Here checking if entered character is vowel or an consonant or neither of it.  
if isVowel in vowel:
    print('Vowel')
elif isVowel in conso:
    print('Consonant')
else:
    print('Invalid Input')




