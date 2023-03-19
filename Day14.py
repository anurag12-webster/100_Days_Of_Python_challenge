num = int(input("Enter a number: "))  # Take input from the user

reverse = 0  # Initialize variable to store reversed number

while num > 0:
    remainder = num % 10  # Get the rightmost digit
    reverse = (reverse * 10) + remainder  # Append the digit to the reversed number
    num //= 10  # Remove the rightmost digit from the original number

print(reverse)  # Print the reversed number
