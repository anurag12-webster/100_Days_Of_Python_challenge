# Get the size of the arrays from the user
size = int(input("Enter the size of the arrays: "))

# Get the elements of the first array from the user
print("Enter the elements of the first array:")
array1 = list(map(int, input().split()))

# Get the elements of the second array from the user
print("Enter the elements of the second array:")
array2 = list(map(int, input().split()))

# Initialize the sum of the maximum scalar products
sum_of_scalar_products = 0

# Iterate over the elements of the arrays and calculate the scalar products
for i in range(size):
    scalar_product = array1[i] * array2[i]
    sum_of_scalar_products += scalar_product

# Print the sum of the maximum scalar products
print("Sum of the maximum scalar products:", sum_of_scalar_products)
