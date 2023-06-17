def dfs(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)


# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the size of X and the number of sets Si
    n, m = map(int, input().split())

    graph = {i: [] for i in range(n)}
    for _ in range(m):
        subset = list(map(int, input().split()))[1:]
        for i in range(len(subset)):
            for j in range(i + 1, len(subset)):
                graph[subset[i]].append(subset[j])
                graph[subset[j]].append(subset[i])

    visited = set()
    connected_components = 0

    for i in range(n):
        if i not in visited:
            dfs(i, graph, visited)
            connected_components += 1

    # Print the minimum number of atoms
    print(connected_components)
