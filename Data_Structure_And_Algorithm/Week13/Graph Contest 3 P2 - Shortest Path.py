import heapq

def shortest_path(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_vertex == end:
            return current_distance
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

N, M = map(int, input().split())
graph = {i: {} for i in range(1, N + 1)}

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

result = shortest_path(graph, 1, N)

print(result)
