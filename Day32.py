def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    vowels_removed = ""
    for char in string:
        if char not in vowels:
            vowels_removed += char
    return vowels_removed

# Get the input string from the user
input_string = input("Enter a string: ")

# Remove vowels from the string
removed_string = remove_vowels(input_string)

# Print the string with vowels removed
print(removed_string)
