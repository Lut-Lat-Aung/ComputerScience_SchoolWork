def largest_cloud_size(matrix):
    def dfs(i, j):
        if i < 0 or i >= M or j < 0 or j >= N or matrix[i][j] == 0:
            return 0
        
        matrix[i][j] = 0
        size = 1
        size += dfs(i + 1, j)
        size += dfs(i - 1, j)
        size += dfs(i, j + 1)
        size += dfs(i, j - 1)
        
        return size

    M, N = len(matrix), len(matrix[0])
    #M is matrix len
    #N is one row len for matrix
    
    max_cloud_size = 0

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                max_cloud_size = max(max_cloud_size, dfs(i, j))

    return max_cloud_size

# Read input
M, N = map(int, input().split())
matrix = []
for _ in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find and print the size of the largest cloud
print(largest_cloud_size(matrix))
