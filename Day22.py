# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

# Find the two prime numbers that sum up to n
for i in range(2, n // 2 + 1):
    if is_prime(i) and is_prime(n - i):
        print(str(n) + " can be expressed as sum of " + str(i) + " and " + str(n - i))
        break
