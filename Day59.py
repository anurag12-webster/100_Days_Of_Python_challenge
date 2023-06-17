# Get the number of test cases from the user
test_cases = int(input())

# Iterate over the test cases
for _ in range(test_cases):
    # Get the input for each test case
    mass, height = map(int, input().split())

    # Calculate the BMI
    bmi = mass / (height ** 2)

    # Determine the category based on the BMI
    if bmi <= 18:
        category = 1
    elif bmi >= 19 and bmi <= 24:
        category = 2
    elif bmi >= 25 and bmi <= 29:
        category = 3
    else:
        category = 4

    # Print the category
    print(category)
