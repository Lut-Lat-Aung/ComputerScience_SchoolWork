
def merge(A, p, q, r):
    # merge the sorted A[p:q+1] with the sorted A[q+1:r+1]
    # the result is a sorted A[p:r+1]
    # Hint: an auxiliary list is required
    # Complete the body of this function

    p = 0
    q = len(A)/2
    r = len(A)
    left = A[p:q-1]
    right = A[q:r]

    mergesort(left,p , q)
    mergesort(right,p , q)


def mergesort(A, p, r):
    # Complete the body of this function
    i = 0
    k = 0
    while i < len(A):
            a[k] = A[i]
            i += 1
            k += 1

a = list(map(int, input().split()))

import time

st = time.process_time()

mergesort(a, 0, len(a)-1)

et = time.process_time()

print(a)
print(et-st)
