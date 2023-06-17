# Get the number of test cases from the user
test_cases = int(input())

# Iterate over the test cases
for _ in range(test_cases):
    # Get the input for each test case
    n, x, p = map(int, input().split())

    # Calculate the total marks
    total_marks = (x * 3) + ((n - x) * (-1))

    # Check if Anusree passes or fails the exam
    if total_marks >= p:
        print("PASS")
    else:
        print("FAIL")
