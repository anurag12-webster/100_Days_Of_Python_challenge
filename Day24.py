def print_pyramid(num_lines):
    for i in range(num_lines):
        print('*' * (2 * i + 1))

num_lines = int(input("Enter the number of lines: "))

print_pyramid(num_lines)
