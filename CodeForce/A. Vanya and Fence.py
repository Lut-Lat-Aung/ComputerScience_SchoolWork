nh = [int(nh) for (nh) in input().split()]
a = [int(a) for a in input().split()]

sum = 0
for i in range(nh[0]):
    if (a[i] > nh[1]):
        sum += 2
    else:
        sum += 1

print(sum)