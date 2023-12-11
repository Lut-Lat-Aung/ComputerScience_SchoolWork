n = int(input())

s = input()

countA = 0
countD = 0
for i in s:
    if i == 'A':
        countA += 1
    if i == 'D':
        countD += 1

if countA > countD:
    print("Anton")
if countD > countA:
    print("Danik")
if countA == countD:
    print("Friendship")