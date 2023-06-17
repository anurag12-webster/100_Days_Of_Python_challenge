def maximum_problem_sets(T):
    for _ in range(T):
        A1, A2, A3, A4 = map(int, input().split())
        difficulties = {A1, A2, A3, A4}
        num_difficulties = len(difficulties)

        if num_difficulties == 4:
            print(2)
        else:
            print(1)


# Read the number of test cases
T = int(input())

# Call the function to solve the problem
maximum_problem_sets(T)
