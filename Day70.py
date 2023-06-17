def rotate_array(arr):
    # Store the last element
    last = arr[-1]

    # Shift all elements to the right
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    # Place the last element at the first position
    arr[0] = last

# Read the size of the array
N = int(input())

# Read the array elements
A = list(map(int, input().split()))

# Rotate the array
rotate_array(A)

# Print the rotated array
print(*A)
