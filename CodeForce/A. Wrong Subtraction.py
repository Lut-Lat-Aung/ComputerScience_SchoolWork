n = [int (n) for (n) in input().split()]

first  = n[0]
last = n[1]

for i in range(last):

    if first%10 == 0:
        first /= 10
        last -= 1
    else:
        first -= 1
        last -= 1

    
    
print(int(first))