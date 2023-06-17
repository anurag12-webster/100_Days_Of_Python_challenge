def is_palindrome(string):
    return string == string[::-1]

def check_palindromic_substrings(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if is_palindrome(A[i:] + B[j:]):
                return True
    return False

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the strings A and B
    A = input()
    B = input()

    # Check if palindromic substrings exist
    if check_palindromic_substrings(A, B):
        print("Yes")
    else:
        print("No")
