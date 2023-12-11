weights = [int(weights) for (weights) in input().split()]

thelist = []
for i in weights:
    thelist.append(i)

#print(thelist)
Limak = thelist[0]
Bob = thelist[1]
count = 0
    
while (Limak <= Bob):
    count+=1
    Limak = Limak*3
    Bob = Bob*2
else:
    print(count)