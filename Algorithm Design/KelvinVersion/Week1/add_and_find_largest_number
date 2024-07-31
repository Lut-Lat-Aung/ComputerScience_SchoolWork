import time
start_time = time.process_time()

numbers = list(map(int, input().split()))

def Sum(num, i, j):
    sm = 0
    for k in range(i, j+1):
        sm += num[k]
    return sm

def find_max_subsequence_sum(numbers):
    total = float('-inf')  # Initialize total as negative infinity
    print(numbers)

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            subsequence_sum = Sum(numbers, i, j)
            print("sum, ", subsequence_sum)
            if subsequence_sum > total:
                total = subsequence_sum
            print("max", total)
    return total

end_time = time.process_time()
mx = find_max_subsequence_sum(numbers)
print(mx)
running_time = end_time - start_time

print("Running time: ", running_time)