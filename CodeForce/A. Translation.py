n1 = input()
n2 = input()

t = len(n2) - 1
count = 0
for i in range(len(n1)):
    if (n1[i] == n2[t]):
        count += 1
        t -= 1

if count == len(n1):
    print("YES")
else:
    print("NO")