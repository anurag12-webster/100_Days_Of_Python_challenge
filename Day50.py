# Get the elements of the array from the user
print("Enter the elements of the array:")
array = list(map(int, input().split()))

# Calculate the sum of positive square elements
sum_positive_squares = sum(x**2 for x in array if x > 0)

# Print the result
print("Sum of positive square elements:", sum_positive_squares)
