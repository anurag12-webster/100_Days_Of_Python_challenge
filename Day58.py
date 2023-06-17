# Get the number of test cases from the user
test_cases = int(input())

# Iterate over the test cases
for _ in range(test_cases):
    # Get the input for each test case
    k, x = map(int, input().split())

    # Calculate the extra water that can be filled
    extra_water = k - x

    # Print the result
    print(extra_water)
