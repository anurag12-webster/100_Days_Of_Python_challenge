num = int(input("Enter a number: "))  
factors = [] 
# Find the factors of the number
for i in range(1, num+1):
    if num % i == 0:
        factors.append(i)
print("The factors of", num, "are:", factors)
