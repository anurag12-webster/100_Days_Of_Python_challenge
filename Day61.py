# Get the number of test cases from the user
test_cases = int(input())

# Iterate over the test cases
for _ in range(test_cases):
    # Get the input for each test case
    a, b = map(int, input().split())

    # Determine the chess format
    if a + b < 3:
        format = 1  # Bullet
    elif 3 <= a + b <= 10:
        format = 2  # Blitz
    elif 11 <= a + b <= 60:
        format = 3  # Rapid
    else:
        format = 4  # Classical

    # Print the chess format
    print(format)
