# Get the number of test cases from the user
test_cases = int(input())

# Iterate over the test cases
for _ in range(test_cases):
    # Get the input for each test case
    weather_report = list(map(int, input().split()))

    # Count the number of sunny and rainy days
    sunny_days = weather_report.count(1)
    rainy_days = weather_report.count(0)

    # Determine if the weather report is good or not
    if sunny_days > rainy_days:
        result = "YES"
    else:
        result = "NO"

    # Print the result
    print(result)
