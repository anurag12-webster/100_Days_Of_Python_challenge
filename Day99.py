def minimum_time_to_clean_floor(T):
    for _ in range(T):
        N, M = map(int, input().split())
        segments = []

        for _ in range(M):
            L, R = map(int, input().split())
            segments.append((L, R))

        segments.sort(key=lambda x: x[0])

        max_end = 0
        time = 0

        for segment in segments:
            L, R = segment
            if L > max_end:
                print(-1)
                break
            max_end = max(max_end, R)
            time = max(time, R)

        else:
            print(time)


# Read the number of test cases
T = int(input())

# Call the function to solve the problem
minimum_time_to_clean_floor(T)
