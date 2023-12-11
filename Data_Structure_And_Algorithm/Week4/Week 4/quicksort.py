import sys
sys.setrecursionlimit(10000)

def partition(A, p, r):  # Lomuto's partition scheme
    counter = 0
    x = A[r]
    i = p-1
    for j in range(p, r):
        counter += 1
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]   
    A[r],A[i+1] = A[i+1],A[r]
    return counter
     



def quickSort(arr, low, high):
    if (low < high):
         
        pi = partition(arr, low, high)
        print(arr[low:pi], arr[pi], arr[pi+1:high+1])
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
         
def printArray(arr, size):
     
    for i in range(size):
        print(arr[i], end = " ")
    print()



arr = [int(arr) for arr in input().split()]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array:")
printArray(arr, n)
print()


A = [int(A) for A in input().split()]
p = 0
r = len(A) - 1
print()
print(partition(A, p, r))
#print(counter)