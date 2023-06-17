def is_palindrome(num):
    # Convert the number to string for comparison
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

def find_longest_palindrome(arr):
    longest_palindrome = None

    for num in arr:
        if is_palindrome(num):
            if longest_palindrome is None or num > longest_palindrome:
                longest_palindrome = num

    return longest_palindrome

# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Get the elements of the array from the user
print("Enter the elements:")
arr = list(map(int, input().split()))

# Find the longest palindrome in the array
longest_palindrome = find_longest_palindrome(arr)

# Print the result
if longest_palindrome is None:
    print("No palindrome found in the array")
else:
    print("Longest palindrome:", longest_palindrome)
