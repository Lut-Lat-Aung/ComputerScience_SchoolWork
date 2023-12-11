
graph_type = input()
if graph_type != "Directed Graph":
    print("DFS only works on Directed Graph")
    exit()

V, E = map(int, input().split())
adj_list = [[] for v in range(V)]

for i in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)

color = ["WHITE"] * V
p = [None] * V
time = 0
d = [-1] * V
f = [-1] * V

# Depth-First Search implementation


def DFS_visit(u):
    global time
    time += 1
    d[u] = time
    color[u] = "GRAY"
    
    for v in adj_list[u]:
        if color[v] == "WHITE":
            p[v] = u
            DFS_visit(v)
    
    color[u] = "BLACK"
    time += 1
    f[u] = time


# Perform DFS on all vertices

for v in range(V):
    if color[v] == "WHITE":
        DFS_visit(v)

# Print the output
for v in range(V):
    if d[v] == -1:
        dv = "undiscovered"
    else:
        dv = d[v]
    
    if f[v] == -1:
        fv = ""
    else:
        fv = f[v]
    
    if p[v] is not None:
        pv = p[v] + 1
    else:
        pv = "None"
    
    print("%d %5s" % (v + 1, color[v]), dv, fv, pv)

