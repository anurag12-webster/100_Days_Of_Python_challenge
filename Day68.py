# Read the number of queries
n = int(input())

# Initialize an empty set
elements = set()

# Process each query
for _ in range(n):
    query_type, num = map(int, input().split())

    # Perform the corresponding operation based on the query type
    if query_type == 1:
        # Add an element to the set
        elements.add(num)
    elif query_type == 2:
        # Delete an element from the set
        elements.discard(num)
    elif query_type == 3:
        # Check if the number is present in the set and print the result
        if num in elements:
            print("Yes")
        else:
            print("No")
