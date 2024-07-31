import random

def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def kth_order_statistic(arr, k):
    p = 0
    r = len(arr) - 1

    while p <= r:
        q = partition(arr, p, r)
        if q == k:
            return arr[q]
        elif k < q:
            r = q - 1
        else:
            p = q + 1

arr = list(map(int, input().split()))
k = int(input())
result = kth_order_statistic(arr, k - 1) 
print(result)


