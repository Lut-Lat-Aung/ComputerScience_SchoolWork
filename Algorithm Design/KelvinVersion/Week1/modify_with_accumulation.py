import time

start_time = time.process_time()

numbers = list(map(int, input().split()))
print(numbers)

def Sum(accumulated, i, j):
    if i == 0:
        return accumulated[j]
    return accumulated[j] - accumulated[i-1]

def find_max_subsequence_sum(numbers):
    accumulated = []
    acc = 0

    for num in numbers:
        acc += num
        accumulated.append(acc)
        
    print(accumulated)

    largest_sum = float('-inf')

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            subsequence_sum = Sum(accumulated, i, j)
            print("subsequence_sum", subsequence_sum)
            print("largest_sum", largest_sum)
            if subsequence_sum > largest_sum:
                largest_sum = subsequence_sum
    return largest_sum

end_time = time.process_time()
mx = find_max_subsequence_sum(numbers)
print(mx)
running_time = end_time - start_time

print("Running time: ", running_time)