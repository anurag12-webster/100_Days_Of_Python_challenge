num = int(input("Enter a number: "))

# Find the factors of the number and add them up
sum_factors = 0
for i in range(1, num):
    if num % i == 0:
        sum_factors += i

# Check if the sum of factors is equal to the original number
if sum_factors == num:
    print(num, "is a Perfect number")
else:
    print(num, "is not a Perfect number")
