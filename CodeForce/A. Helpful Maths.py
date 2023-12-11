Letter = (input())

#print(Letter)

count = 0
thelist = []
for i in range(len(Letter)):
    if (Letter[i] == "+") :
        count += 0
    else:
        thelist.append(Letter[i])

thelist.sort()
#print(thelist)
for i in range((len(thelist))-1):
    print(thelist[i] + "+", end = "")

print(thelist[len(thelist)-1])