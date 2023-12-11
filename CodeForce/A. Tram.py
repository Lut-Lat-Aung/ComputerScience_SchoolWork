n = int(input())
thexit = []
thent = []
for i in (range(n)):
    mat = [int(n) for n in input().split()]
    
    
    thexit.append(mat[0])
    thent.append(mat[1])

tn = thent[0] - thexit[1]
out = tn + thent[1]

yin = []
yin.append(out)
yin.append(thent[0])
for j in range(n-2):
    tn = out - thexit[j+2]
    out = tn + thent[j+2]
    yin.append(out)

yin.sort()
yin.reverse()
print(yin[0])
#print(out)