def find_array_type(arr):
    # Initialize counters for even and odd elements
    even_count = 0
    odd_count = 0

    # Iterate through the array elements
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Determine the array type based on the counts
    if even_count == 0:
        return "Odd"
    elif odd_count == 0:
        return "Even"
    else:
        return "Mixed"

# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Get the elements of the array from the user
print("Enter the elements:")
arr = list(map(int, input().split()))

# Find the type of the array
array_type = find_array_type(arr)

# Print the result
print(array_type)
