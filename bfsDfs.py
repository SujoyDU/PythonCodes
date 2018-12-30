#Graph in adjacency list

graph = { 
            'A': set(['B', 'C']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A', 'F']),
            'D': set(['B']),
            'E': set(['B', 'F']),
            'F': set(['C', 'E'])
        }



def dfs(graph, start, visited = set(), Nodelist = []):
    if start not in visited:
        Nodelist.append(start)
        visited.add(start)

    print(Nodelist)
    for next in graph[start] - visited:
        dfs(graph,next,visited,Nodelist)
    return visited


def bfs(graph, start, visited = set(), Nodelist = []):
    Nodelist.append(start)
    while Nodelist:
        node = Nodelist.pop(0)
        visited.add(node)
        for next in graph[node] - visited:
            print(f'{node} --> {next}')
            Nodelist.append(next)



bfs(graph,'A')
print(dfs(graph,'C'))