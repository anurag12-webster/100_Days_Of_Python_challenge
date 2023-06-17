def eat_candy(N, K):
    bites = 0

    while N > 0:
        if N >= K:
            N -= K
            bites += 1
        else:
            bites = -1
            break

    return bites


# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the parameters N and K
    N, K = map(int, input().split())

    # Calculate and print the minimum number of bites
    bites = eat_candy(N, K)
    print(bites)
