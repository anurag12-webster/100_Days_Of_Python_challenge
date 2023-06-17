# Get the size of the first array from the user
size1 = int(input("Enter the size of the first array: "))

# Get the elements of the first array from the user
print("Enter the elements of the first array:")
array1 = list(map(int, input().split()))

# Get the size of the second array from the user
size2 = int(input("Enter the size of the second array: "))

# Get the elements of the second array from the user
print("Enter the elements of the second array:")
array2 = list(map(int, input().split()))

# Initialize a flag variable to track whether arrays are disjoint or not
disjoint = True

# Iterate over the elements of the first array
for element1 in array1:
    # Check if the current element exists in the second array
    if element1 in array2:
        disjoint = False
        break

# Print the result based on the disjoint flag
if disjoint:
    print("Disjoint")
else:
    print("Not disjoint. Common elements exist.")
