def find_different_string(test_cases):
    for case in test_cases:
        n = int(input())
        strings = []
        for _ in range(n):
            strings.append(input())

        different_string = ''
        for i in range(n):
            if strings[0][i] == '0':
                different_string += '1'
            else:
                different_string += '0'

        print(different_string)

# Read the number of test cases
t = int(input())

# Read the test cases
test_cases = []
for _ in range(t):
    test_cases.append(input())

# Solve and print the result
find_different_string(test_cases)
