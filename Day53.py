# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Get the elements of the array from the user
print("Enter the elements of the array:")
array = list(map(int, input().split()))

# Initialize variables to track the maximum product
max_product = array[0]
current_max = array[0]
current_min = array[0]

# Iterate over the array
for i in range(1, size):
    # Update the current maximum and minimum products
    if array[i] < 0:
        current_max, current_min = current_min, current_max
    
    current_max = max(array[i], current_max * array[i])
    current_min = min(array[i], current_min * array[i])
    
    # Update the maximum product if needed
    max_product = max(max_product, current_max)

# Print the maximum product subarray
print("Maximum product subarray:", max_product)
