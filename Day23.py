def replace_zeros_with_ones(number):
    new_number = ""
    for digit in str(number):
        if digit == "0":
          new_number += "1"
        else:
          new_number += digit

        return int(new_number)


if __name__ == "__main__":
  number = input("Enter a number: ")
  new_number = replace_zeros_with_ones(number)
  print("The number with zeros replaced with ones is:", new_number)
