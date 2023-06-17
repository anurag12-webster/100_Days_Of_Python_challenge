# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of students
    N = int(input())

    # Read the scores of the students
    scores = list(map(int, input().split()))

    # Initialize the count of boasting students
    boasting_count = 0

    # Iterate through each student
    for i in range(N):
        less_count = 0
        greater_count = 0

        # Compare the score of the current student with all other students
        for j in range(N):
            if scores[j] <= scores[i]:
                less_count += 1
            if scores[j] > scores[i]:
                greater_count += 1

        # Check if the student will boast
        if less_count > greater_count:
            boasting_count += 1

    # Print the number of boasting students for the current test case
    print(boasting_count)
