def biggest_descendent(graph, root, value):

    biggest = {}

    def dfs(node):

        max_value = value[node]

        for child in graph.neighbors(node):
            max_value = max(max_value, dfs(child))

        biggest[node] = max_value
        return max_value

    dfs(root)

    return biggest