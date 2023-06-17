def calculate_max_steps(N, K, C, nums):
    nums.sort()
    steps = 0

    for i in range(N):
        if i + K >= N:
            break

        valid = True
        for j in range(i + 1, i + K + 1):
            if nums[j] < nums[j - 1] * C:
                valid = False
                break

        if valid:
            steps += 1
            i += K

    return steps

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read N, K, and C for each test case
    N, K, C = map(int, input().split())
    # Read the initial numbers
    nums = list(map(int, input().split()))
    # Calculate the maximum number of steps
    result = calculate_max_steps(N, K, C, nums)
    # Print the result
    print(result)
