def check_anagram(string1, string2):
    # Convert the strings to lowercase and remove whitespace
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    # Check if the sorted characters of the strings are equal
    return sorted(string1) == sorted(string2)

# Get the input strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams
is_anagram = check_anagram(string1, string2)

# Print the result
if is_anagram:
    print("Anagram")
else:
    print("Not an Anagram")
