def countPythagoreanTriples(tree_nodes, tree_from, tree_to, x, y, z):
    # Create an adjacency list representation of the tree
    graph = [[] for _ in range(tree_nodes)]
    for i in range(tree_nodes - 1):
        graph[tree_from[i]].append(tree_to[i])
        graph[tree_to[i]].append(tree_from[i])

    def dfs(node, parent):
        nonlocal count
        nonlocal distances

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)

        # Calculate distances from the current node to x, y, and z
        distances_x = 0 if node != x else 1
        distances_y = 0 if node != y else 1
        distances_z = 0 if node != z else 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            distances_x += distances[neighbor][0]
            distances_y += distances[neighbor][1]
            distances_z += distances[neighbor][2]

        # Check if the distances form a Pythagorean triple
        if (
            (distances_x ** 2 + distances_y ** 2 == distances_z ** 2) or
            (distances_y ** 2 + distances_z ** 2 == distances_x ** 2) or
            (distances_z ** 2 + distances_x ** 2 == distances_y ** 2)
        ):
            count += 1

        # Update the distances for the current node
        distances[node] = (distances_x, distances_y, distances_z)

    count = 0
    distances = [(0, 0, 0)] * tree_nodes
    dfs(x, -1)  # Start DFS from node x
    print("Number of Pythagorean Triples:", count)
    return count

# Example usage:
tree_nodes = 9
tree_from = list(range(8))
tree_to = list(range(1, 9))
x = 3
y = 4
z = 5
result = countPythagoreanTriples(tree_nodes, tree_from, tree_to, x, y, z)