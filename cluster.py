def cluster(graph, weights, level):

    visited = set()
    clusters = []

    def dfs(node, component):
        visited.add(node)
        component.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited and weights(node, neighbor) >= level:
                dfs(neighbor, component)

    for node in graph.nodes:
        if node not in visited:
            component = set()
            dfs(node, component)
            clusters.append(frozenset(component))

    return frozenset(clusters)