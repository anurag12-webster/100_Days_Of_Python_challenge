def find_sum(arr):
    total_sum = 0

    for num in arr:
        total_sum += num

    return total_sum

# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Get the elements of the array from the user
print("Enter the elements:")
arr = list(map(int, input().split()))

# Find the sum of the elements
array_sum = find_sum(arr)

# Print the result
print("Sum:", array_sum)
