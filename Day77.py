T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    max_value = float('-inf')

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if k == i or k == j:
                    continue
                value = (A[i] - A[j]) * A[k]
                max_value = max(max_value, value)

    print(max_value)
