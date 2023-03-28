n = int(input())


if n < 2:
    print(str(n) + " is not a prime number")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(str(n) + " is a prime number")
    else:
        print(str(n) + " is not a prime number")
