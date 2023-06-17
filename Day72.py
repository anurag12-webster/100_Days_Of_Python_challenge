# Read the number of queries
Q = int(input())

# Initialize an empty string
S = []

# Process each query
for _ in range(Q):
    query = input().split()

    if query[0] == '+':
        # Insert the string x into the current string S
        i = int(query[1])  # Position to insert
        x = query[2]  # String to insert

        if i == 0:
            S = [ch for ch in x] + S
        else:
            S = S[:i] + [ch for ch in x] + S[i:]
    elif query[0] == '?':
        # Print the substring of length len starting at position i of S
        i = int(query[1])  # Starting position
        length = int(query[2])  # Length of substring

        print(''.join(S[i:i+length]))
