
n = int(input())

# Converting the number to a string to find the number of digits
n_str = str(n)
num_digits = len(n_str)

# Calculate the sum of the digits raised to the power of the number of digits
digit_sum = sum(int(digit)**num_digits for digit in n_str)

if digit_sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
