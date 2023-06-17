# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Get the elements of the array from the user
print("Enter the elements of the array:")
array = list(map(int, input().split()))

# Sort the array in ascending order
sorted_array = sorted(array)

# Print the sorted array
print("Sorted array:", ' '.join(map(str, sorted_array)))
