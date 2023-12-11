

def toAdjLists(M, V):
    # returns collection of adjacency lists
    # Complete this function!
   
    if i in M:
        a, b = M[i]
        c, d = M[i], M[j]
        if a != b and a != c and a != d and b != c and b != d and c != d:
            return (a, b, c, d)
    else:
        M[i] = (M[i], M[j])
    return None

# Read input sequence of distinct integers
M = list(map(int, input().split()))

# Find pairs and print the output
result = toAdjLists(M)
if result:
    print(f"{result[0]} {result[1]}, {result[2]} {result[3]}")
else:
    print("No pair exists")



def printAdjLists(A):
    i = 0
    for l in A:
        print(i, l)
        i += 1

V = int(input())
M = []
for i in range(V):
    aRow = list(map(int, input().split()))
    M.append(aRow)
adjLists = toAdjLists(M, V)
printAdjLists(adjLists)
    

    
