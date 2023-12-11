n = [int(n) for (n) in input().split()]

s = str(input())
i = 0
new = s

for i in range(len(s)):
   if((s[i]=='B') & (s[i+1]=='G')) :
         tmp = s[i]
         s[i] = s[i+1]
         s[i+1] = tmp
         i+=2
   else:
      i+= 1
          
print(s)

'''new = s.split()
n1 = [0] * n[0]


if s[n[1]] == 'G':
   new[0] [n[1]] == 'B'
   #n1.append('B')
   n1.remove(0)
   n1[n[1]] == 'B'

"""""
for i in range(n[0]-1):
    for j in range(n[1]):
        if s[i] == 'B':
            new[i] = 'G'
            new[i+1] = 'B'
"""

print(s[n[1]])
print(new)

for i in new:
   print(i)

print(n1)'''