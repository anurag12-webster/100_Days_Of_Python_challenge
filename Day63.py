# Get the number of test cases from the user
test_cases = int(input())

# Iterate over the test cases
for _ in range(test_cases):
    # Get the input for each test case
    w1, w2, x1, x2, M = map(int, input().split())

    # Calculate the minimum and maximum possible weight increase after M months
    min_increase = x1 * M
    max_increase = x2 * M

    # Check if the measured weight falls within the possible range
    if w2 >= w1 + min_increase and w2 <= w1 + max_increase:
        result = 1
    else:
        result = 0

    # Print the result
    print(result)
