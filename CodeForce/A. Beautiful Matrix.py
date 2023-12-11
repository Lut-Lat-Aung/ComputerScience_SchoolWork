count = 0


for i in range (5):
    n = [int(n) for n in input().split()]

    
    for j in range(5):
        if (n[j] == 1):
            if (j != 2):
                while (j > 2):
                    count += 1
                    j -= 1
                while (j < 2):
                    count += 1
                    j += 1
                
            if (i != 2):
                while (i > 2):
                    
                    count += 1
                    i -= 1
                while (i < 2):

                    count += 1
                    i += 1
    
print(count)
