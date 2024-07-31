import sys
sys.setrecursionlimit(1000000)

tiles = [1, 83, 27, 189, 234]
v = 967
counter = 0
calls = [0] * (v+1)
memo = [None] * (v+1)

def mintile(v):
    global counter
    mintiles = float('inf')

    if memo[v] is not None:
        return memo[v]

    if v == 0:
        return 0
    
    for coin in tiles:
        remaining = v - coin
        if remaining >= 0:
            numCoins = mintile(remaining) + 1
            mintiles = min(mintiles, numCoins)
        memo[v] = mintiles
    
    counter += 1
    calls[v] += 1
    return mintiles

result = mintile(v)
print(f"Result = {result}, {counter} calls")
print("Number of calls for each minTiles():", calls[1:])
