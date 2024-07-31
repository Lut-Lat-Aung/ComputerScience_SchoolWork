m, n = map(int, input().split())

stocks = []
for _ in range(n):
    price, profit = map(int, input().split())
    stocks.append((profit, price))

stocks.sort(key=lambda x: x[0] / x[1], reverse=True)

max_profit = 0
remaining_budget = m

for profit, price in stocks:
    if remaining_budget >= price:
        max_profit += profit
        remaining_budget -= price
    else:
        max_profit += (remaining_budget / price) * profit
        break

print(int(max_profit))
