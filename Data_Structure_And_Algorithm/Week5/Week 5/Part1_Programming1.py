s1 = list(map(str, input().split()))
s2 = list(map(str, input().split()))

new = []

count = 0

s1.sort()
s2.sort()

for i in s2:
    for j in s1:
        if i == j:
            count += 1
            new.append(i)

        elif i != j:
            count -= 1
            
            


#if count == len(s2):
  #  print("Yes")
#else:
 #   print("No")

if new == s2:
    print("Yes")
else:
    print("No")