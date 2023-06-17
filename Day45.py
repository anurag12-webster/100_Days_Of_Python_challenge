def find_smallest_largest(arr):
    smallest = arr[0]
    largest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest

# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Get the elements of the array from the user
print("Enter the elements:")
arr = list(map(int, input().split()))

# Find the smallest and largest element
smallest, largest = find_smallest_largest(arr)

# Print the result
print("Smallest Number:", smallest)
print("Largest Number:", largest)
