def count_inversions(arr):

    # Count the number of inversions in the array

    inversions = 0

    for i in range(len(arr)):

        for j in range(i + 1, len(arr)):

            if arr[i] > arr[j]:

                inversions += 1

    return inversions

 

 

def min_swaps_to_goal(input_config, goal_config):

    # Count inversions in both configurations

    inversions_input = count_inversions(input_config)

    inversions_goal = count_inversions(goal_config)

 

    # Calculate the minimum number of swaps needed

    return abs(inversions_input - inversions_goal)

 

 

# Read input

input_config = list(map(int, input().split()))

goal_config = list(map(int, input().split()))

 

# Calculate and print the minimum number of swaps

min_swaps = min_swaps_to_goal(input_config, goal_config)

print(min_swaps)