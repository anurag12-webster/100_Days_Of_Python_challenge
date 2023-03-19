num = int(input("Enter a number: ")) 
# Calculate the factorial of each digit and add them up
sumo = 0
temp = num
while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit+1):
        factorial *= i
    sumo += factorial
    temp //= 10

# Check if the sum of factorials is equal to the original number
if sumo == num:
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")
