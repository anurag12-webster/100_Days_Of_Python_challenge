# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Get the elements of the array from the user
print("Enter the elements of the array:")
array = list(map(int, input().split()))

# Find the greatest common divisor (GCD) of all the numbers
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

common_factor = array[0]
for i in range(1, size):
    common_factor = gcd(common_factor, array[i])

# Check if all the numbers can be made equal
can_be_equal = True
for num in array:
    if num % common_factor != 0:
        can_be_equal = False
        break

# Print the result
if can_be_equal:
    print("Yes")
else:
    print("No")
