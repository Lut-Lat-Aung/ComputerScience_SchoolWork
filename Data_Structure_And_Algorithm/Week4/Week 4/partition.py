
def partition(A, p, r):  # Lomuto's partition scheme
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]   
    A[r],A[i+1] = A[i+1],A[r]
    return i+1

A = [2,9,3,7,5,6]
p = 0
r = len(A) - 1
print(partition(A, p, r))
