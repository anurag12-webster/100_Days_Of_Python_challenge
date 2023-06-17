# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Get the elements of the array from the user
print("Enter the elements:")
arr = list(map(int, input().split()))

# Create a set from the array to remove duplicates
unique_arr = list(set(arr))

# Print the result
print("Array with duplicates removed:", ' '.join(map(str, unique_arr)))
