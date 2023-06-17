def count_even_odd_elements(arr):
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Get the elements of the array from the user
print("Enter the elements:")
arr = list(map(int, input().split()))

# Count the number of even and odd elements
even_count, odd_count = count_even_odd_elements(arr)

# Print the result
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)
