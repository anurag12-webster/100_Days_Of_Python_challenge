# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the dimensions of the grid
    N, M = map(int, input().split())

    # Calculate the total number of cells in the grid
    total_cells = N * M

    # Check if the grid has an odd number of cells
    if total_cells % 2 == 1:
        # Print 1 as we need one 1x1 tile to cover the extra cell
        print(1)
    else:
        # Print 0 as we can cover all cells using only 2x2 tiles
        print(0)
