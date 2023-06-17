T = int(input())

for _ in range(T):
    N = int(input())
    S = input()

    operations = 0

    for i in range(1, N):
        if S[i] == '1' and S[i-1] == '0':
            operations += 1

    print(operations)
