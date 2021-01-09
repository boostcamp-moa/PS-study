n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

d = [10001] * (m + 1)

d[0] = 0

for coin in coins:
    for i in range(coin, m + 1):
        if d[i - coin] != 10001:
            d[i] = min(d[i], d[i - coin] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
