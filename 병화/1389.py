import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b:
            graph[a][b] = 0

# 방향이 없는 그래프이므로 x, y와 y, x 동시에 설정
for _ in range(e):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# 플로이드 워셜 알고리즘 수행
for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 유저마다 케빈 베이컨 수 계산
result = [0] * (v + 1)
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i != j:
            result[i] += graph[i][j]

# 0번째 인덱스는 제외
print(result.index(min(result[1:])))
