def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

input_string = input("Enter a string: ")

reversed_string = reverse_string(input_string)

print(reversed_string)
