def is_palindrome(string):
    reversed_string = string[::-1]
    if string.lower() == reversed_string.lower():
        return True
    else:
        return False

# Get the input string from the user
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print("Palindrome")
else:
    print("Not a Palindrome")
