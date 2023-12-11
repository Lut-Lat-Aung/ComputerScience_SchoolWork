n = input()

first  = n[0]
if n[0].islower :
    first = first.upper()

print(first + n[1:len(n)])