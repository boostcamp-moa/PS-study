v, e = map(int, input().split())
INF = int(1e9)

# 노드끼리의 연결 상태를 나타내는 2차원 배열 초기화
graph = [[INF] * (v + 1) for _ in range(v + 1)]

# 자기 자신과 연결되는 비용은 0으로 초기화
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b:
            graph[a][b] = 0

# 노드끼리의 연결 상태를 입력 받아 graph 업데이트
for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 경유할 노드 x와 최종 노드 k 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for m in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][m] + graph[m][b])

# 결과 출력
cost = graph[1][k] + graph[k][x]
if cost >= INF:
    print(-1)
else:
    print(cost)
