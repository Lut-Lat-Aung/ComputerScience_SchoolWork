
import time

a = list(map(int, input().split()))

n = len(a)

st = time.process_time()

for i in range(1, n):
        key = a[i] #11 = a[1]
        j = i - 1   #12 / j = 0
               
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key
et = time.process_time()

print(a)
print(et-st)
