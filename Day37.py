def calculate_frequency(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

# Get the input string from the user
input_string = input("Enter a string: ")

# Calculate the frequency of characters in the string
frequency = calculate_frequency(input_string)

# Print the frequency of characters
for char, count in frequency.items():
    print(f"The frequency of {char} is {count}")
