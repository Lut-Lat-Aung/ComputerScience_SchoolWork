def max_token_value(h, w, grid):
    memo = [[0] * w for _ in range(h)]
    memo[0] = grid[0]

    for i in range(1, h):
        for j in range(w):
            max_val = grid[i][j]
            for dj in [-1, 0, 1]:
                nj = j + dj
                if 0 <= nj < w:
                    max_val = max(max_val, grid[i][j] + memo[i - 1][nj])

            memo[i][j] = max_val

    return max(memo[-1])

h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
result = max_token_value(h, w, grid)
print(result)
