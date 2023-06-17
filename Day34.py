def remove_brackets(expression):
    without_brackets = ""
    for char in expression:
        if char != '(' and char != ')':
            without_brackets += char
    return without_brackets

# Get the input algebraic expression from the user
input_expression = input("Enter an algebraic expression: ")

# Remove brackets from the expression
expression_without_brackets = remove_brackets(input_expression)

# Print the expression without brackets
print(expression_without_brackets)
