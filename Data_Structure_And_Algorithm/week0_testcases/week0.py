n = int(input())

i = 1
while (i < n+1):
    print(i, end = " ")
    i += 1

print()
x = [int(x) for x in input().split()]
print(x)

t = -1
oddnum = []
evennum = []
for i in x:
    y = i%2
    if y == 1:
        oddnum.append(i)

    if (y == 0):
        evennum.append(i)
        reverseeven = evennum[::-1]
    if (y == 0 and i > t):
        t = i
    

print(oddnum)
print(t)
print(reverseeven)