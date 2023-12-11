n = input()

thelist = {}

#for i in range(len(n)):
#    thelist.append(n[i])

for j in n:
    if j not in thelist:
        thelist[j] = 1
    else:
        thelist[j] += 1
sum = 0
for t, count in thelist.items():
    if (count > 1):
        sum += 1
    else:
        sum += 1

if (sum%2 == 0) :
    print("CHAT WITH HER!")

else:
    print("IGNORE HIM!")
#if (sum%2 == 0):
 #   print("CHAT WITH HER!")

#else:
  #  print("IGNORE HIM!")
