# Get input fractions
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# Add fractions
x3 = (x1 * y2) + (x2 * y1)
y3 = y1 * y2

# finding the GCD
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# simplifying
g = gcd(x3, y3)
x3 //= g
y3 //= g


print(str(x3) + '/' + str(y3))
