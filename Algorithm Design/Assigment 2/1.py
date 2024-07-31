def count_tilings_recursive(n):
    if n == 0:
        return 1
    if n < 0 or n % 2 == 1:
        return 0
    return 3 * count_tilings_recursive(n - 2) + sum(2 * count_tilings_recursive(n - i) for i in range(4, n + 1, 2))

# Read input and process test cases
while True:
    n = int(input())
    if n == -1:
        break
    result = count_tilings_recursive(n)
    print(result)
