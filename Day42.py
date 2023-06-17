def check_arrays_same(arr1, arr2):
    # Check if the lengths of the arrays are equal
    if len(arr1) != len(arr2):
        return False

    # Sort the arrays
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)

    # Check if the sorted arrays are the same
    return sorted_arr1 == sorted_arr2

# Get the sizes of the arrays from the user
size1 = int(input("Enter the size of the first array: "))
size2 = int(input("Enter the size of the second array: "))

# Get the elements of the first array from the user
print("Enter elements of the first array:")
arr1 = list(map(int, input().split()))

# Get the elements of the second array from the user
print("Enter elements of the second array:")
arr2 = list(map(int, input().split()))

# Check if the arrays are the same
is_same = check_arrays_same(arr1, arr2)

# Print the result
if is_same:
    print("Same")
else:
    print("Not the same")
