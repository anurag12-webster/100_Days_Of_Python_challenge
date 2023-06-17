T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    sum_weights = 0
    weight = 0

    for i in range(N - 2):
        weight += (A[i] - A[i + 1]) * (A[i + 1] - A[i + 2])
        sum_weights += weight

    print(sum_weights)
