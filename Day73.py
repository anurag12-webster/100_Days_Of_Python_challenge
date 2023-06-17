# Function to check if a substring is boring
def is_boring(substring):
    return len(set(substring)) == 1

# Function to find the length of the longest boring substring that occurs more than once
def find_longest_boring_substring(S):
    N = len(S)
    longest_boring_length = 0

    # Iterate through all possible substrings
    for i in range(N):
        for j in range(i+1, N+1):
            substring = S[i:j]

            # Check if the substring is boring and occurs more than once
            if is_boring(substring) and S.count(substring) > 1:
                longest_boring_length = max(longest_boring_length, len(substring))

    return longest_boring_length

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the length of the string and the string itself
    N = int(input())
    S = input()

    # Find the length of the longest boring substring that occurs more than once
    longest_boring_length = find_longest_boring_substring(S)

    # Print the result for the current test case
    print(longest_boring_length)
