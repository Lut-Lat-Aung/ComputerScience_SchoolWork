n = [int(n) for (n) in input().split()]


thelist = []

for i in n:
    thelist.append(i)

first = thelist[0]
sum = 0
for k in range(thelist[2]):
    
    first = thelist[0]*(k+1)

    #print(first)
    sum += first

if (sum > thelist[1]):
    print(sum-thelist[1])
else:
    print(0)