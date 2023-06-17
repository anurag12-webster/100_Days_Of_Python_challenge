def find_non_repeating_chars(string):
    non_repeating_chars = []

    for char in string:
        if string.count(char) == 1:
            non_repeating_chars.append(char)

    return non_repeating_chars

# Get the input string from the user
input_string = input("Enter a string: ")

# Find the non-repeating characters in the string
non_repeating_chars = find_non_repeating_chars(input_string)

# Print the non-repeating characters
for char in non_repeating_chars:
    print(char, end=" ")

print()  # Print a new line
