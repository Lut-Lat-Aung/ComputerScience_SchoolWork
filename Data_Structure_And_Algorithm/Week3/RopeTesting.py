import time
n = [int(n) for n in input().split()]

total = 0

n.sort()
st = time.process_time()
i = 0


cost = n[i] + n[i+1]
while i < (len(n)/2):
    
    total += cost
    cost = cost + n[i+2]
    i += 1

total += cost

en = time.process_time()
print(total)
print(en - st)