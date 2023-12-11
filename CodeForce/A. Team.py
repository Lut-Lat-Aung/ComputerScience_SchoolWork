n = int(input())

count = 0
for i in range(n):
    multiTest = [int(multiTest) for multiTest in input().split()]
    
    if (multiTest[0] == 1):
        if (multiTest[1] == 1):
            count += 1

        elif (multiTest[2] == 1):
            count += 1
            
    elif (multiTest[1] == 1) :
        if (multiTest[2] == 1) :
            count += 1

print(count)