N = int(input())
answer = [0] * (N + 1)

for i in range(1, N + 1):
    if i == 1:
        continue
    temp = []
    if i % 3 == 0:
        temp.append(answer[i // 3] + 1)
    if i % 2 == 0:
        temp.append(answer[i // 2] + 1)
    temp.append(answer[i - 1] + 1)
    answer[i] = min(temp)

print(answer[N])
