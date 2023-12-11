s1 = list(map(str, input().split()))
s2 = list(map(str, input().split()))

for i in s1:
    for j in s2:
        if i == j:
            s1.remove(str(i))

print(s1)
print(len(s1))

for i in (range(len(s1)):
    print(i)