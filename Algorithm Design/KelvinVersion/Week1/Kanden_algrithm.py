import time

start_time = time.process_time()

numbers = list(map(int, input().split()))

def kadane_algorithm(numbers):
    max_sum = float('-inf')
    current_sum = 0
    print(numbers)
    for num in numbers:
        print("number = ", num)
        current_sum = max(num, current_sum + num)
        print("Current sum", current_sum)
        max_sum = max(max_sum, current_sum)
        print("Max sum ------", max_sum)
    return max_sum

end_time = time.process_time()
mx = kadane_algorithm(numbers)
print(mx)
running_time = end_time - start_time

print("Running time: ", running_time)