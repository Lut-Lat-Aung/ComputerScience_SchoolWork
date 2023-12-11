n = int(input())

seq_order = []

for i in range(n):
    sequence = list(map(str, input().split()))


for j in range(3):
    seq_order.append(sequence[3])

seq_order.sort()

