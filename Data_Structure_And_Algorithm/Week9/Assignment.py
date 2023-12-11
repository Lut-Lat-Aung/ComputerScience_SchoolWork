def DFS_visit(s, adj):
    global visited, stack
    
    for v in adj[s]:
        if not visited[v]:
            visited[v] = True
            DFS_visit(v, adj)
    stack.append(s)

def topological_sort(V, adj):
    global visited, stack
    
    visited = [False] * V
    stack = []
    
    for s in range(V):
        if not visited[s]:
            visited[s] = True
            DFS_visit(s, adj)
    
    stack.reverse()
    return stack

def main():
    V, E = map(int, input().split())
    adj = [[] for _ in range(V)]

    for _ in range(E):
        source, target = map(int, input().split())
        adj[source].append(target)

    sorted_vertices = topological_sort(V, adj)
    for vertex in sorted_vertices:
        print(vertex)

if __name__ == "__main__":
    main()