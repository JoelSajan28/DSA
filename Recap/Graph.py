from collections import deque

class Graph():
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append[u]
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:

            node = queue.popleft()
            if node not in visited:
                print(node)
                visited.add(node)
            
                for neighbour in self.graph[node]:   
                    queue.append(neighbour)
    
    def dfs(self, graph, node, visited):
        if node in visited:
            return
        print(node)
        visited.add(node)

        for neighbour in graph[node]:
            self.dfs(graph, neighbour, visited)




