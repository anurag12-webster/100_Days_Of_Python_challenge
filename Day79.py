T = int(input())

for _ in range(T):
    N = int(input())
    S = input()

    operations = 0

    for i in range(N):
        if S[i] == '1':
            operations += 1
            if i + 1 < N:
                i += 1  # Skip the next character

    print(operations)
