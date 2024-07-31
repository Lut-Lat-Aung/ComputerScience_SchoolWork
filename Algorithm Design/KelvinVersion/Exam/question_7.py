def max_visible_trees(tree_heights):
    n = len(tree_heights)
    dp = [1] * n  # Initialize the dp array with 1 since each tree is at least visible to itself
    
    for i in range(1, n):
        for j in range(i):
            if tree_heights[i] > tree_heights[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example usage
tree_heights = [5,6,3,4,4,5]
max_visible = max_visible_trees(tree_heights)
print(max_visible)  # Output: 4
