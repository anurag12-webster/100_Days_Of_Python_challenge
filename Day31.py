def toggle_string(string):
    toggled_string = ""
    for char in string:
        if char.islower():
            toggled_string += char.upper()
        elif char.isupper():
            toggled_string += char.lower()
        else:
            toggled_string += char
    return toggled_string

# Get the input string from the user
input_string = input("Enter a string: ")

# Toggle the string
toggled_string = toggle_string(input_string)

# Print the toggled string
print(toggled_string)
