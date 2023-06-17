# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Get the elements of the array from the user
print("Enter the elements of the array:")
array = list(map(int, input().split()))

# Reverse the array
reversed_array = array[::-1]

# Print the reversed array
print("Reversed array:", ' '.join(map(str, reversed_array)))
