n = int(input())

n_str = str(n)
n_str_reversed = n_str[::-1]

# Check if the reversed string is equal to the original string
if n_str == n_str_reversed:
    print("Palindrome")
else:
    print("Not a Palindrome")
