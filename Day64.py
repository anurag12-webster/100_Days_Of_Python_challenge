# Get the number of test cases from the user
test_cases = int(input())

# Iterate over the test cases
for _ in range(test_cases):
    # Get the feedback string for each test case
    feedback = input()

    # Check if the feedback string contains the required substrings
    if "010" in feedback or "101" in feedback:
        print("Good")
    else:
        print("Bad")
