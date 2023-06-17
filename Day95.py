# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the integer N
    N = int(input())

    # Initialize the number of operations
    operations = 0

    # Break N into powers of 2
    while N > 0:
        if N % 2 == 1:
            N -= 1
            operations += 1
        N //= 2

    # Print the minimum number of operations
    print(operations)
