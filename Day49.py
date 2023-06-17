# Get the size of the arrays from the user
size = int(input("Enter the size of the arrays: "))

# Get the elements of the first array from the user
print("Enter the elements of the first array:")
array1 = list(map(int, input().split()))

# Get the elements of the second array from the user
print("Enter the elements of the second array:")
array2 = list(map(int, input().split()))

# Calculate the dot product
dot_product = sum(x * y for x, y in zip(array1, array2))

# Print the result
print("Minimum scalar product:", dot_product)
    