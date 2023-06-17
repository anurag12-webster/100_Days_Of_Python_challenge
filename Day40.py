def replace_substring(string, old_substring, new_substring):
    # Check if the old substring exists in the string
    if old_substring in string:
        # Replace the old substring with the new substring
        new_string = string.replace(old_substring, new_substring)
        return new_string
    else:
        # If the old substring is not found, return the original string
        return string

# Get the input string from the user
input_string = input("Enter a string: ")

# Get the substring to be removed from the user
old_substring = input("Enter the substring to be removed: ")

# Get the new substring from the user
new_substring = input("Enter the new substring: ")

# Replace the substring in the string
new_string = replace_substring(input_string, old_substring, new_substring)

# Print the new string
print("The new string:")
print(new_string)
