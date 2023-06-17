# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of S, W1, W2, W3
    S, W1, W2, W3 = map(int, input().split())

    # Calculate the sum of the widths
    W = W1 + W2 + W3

    # Check the conditions and print the minimum required number of hits
    if W <= S:
        print(1)
    elif max(W1, W2, W3) > S and min(W1, W2, W3) > S:
        print(3)
    else:
        print(2)
