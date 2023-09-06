import collections

graph = {
    'a': ['b', 'd'],
    'b': ['a', 'c'],
    'c': ['b', 'f'],
    'd': ['a', 'e', 'f'],
    'e': ['d', 'f', 'g'],
    'f': ['d', 'e', 'h', 'c'],
    'g': ['e', 'h'],
    'h': ['f', 'g']
}


def bfs(g, root):
    # takes im graph and root
    queue = collections.deque([root])
    # creates the queue
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            # if node is in visited
            visited.append(node)
            # if it hasn't then it adds node to visited
        for item in g[node]:
            # iterates through graph
            if item not in visited:
                # if item is in visited
                queue.append(item)
                # adds it to the queue
    print(visited)


bfs(graph, 'a')
