def calculate_length(string):
    length = 0
    for char in string:
        length += 1
    return length

# Get the input string from the user
input_string = input("Enter a string: ")

# Calculate the length of the string
length = calculate_length(input_string)

# Print the length of the string
print(length)
