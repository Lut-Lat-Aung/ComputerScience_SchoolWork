n = int(input())


#print(isinstance(n, int)) it give output True or False

thelist = []
for i in range(n):
    
    w = str(input())
    thelist.append(w)

for i in thelist:
    length = str(len(i)-2)
    if (len(i) > 10) :
        print(i[0] +  length   + i[len(i)-1])
    else:
        print(i)

#print(thelist)