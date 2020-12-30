N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

# 인접 행렬로 변환
for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1


def dfs(vertex):
    visited[vertex] = True
    print(vertex, end=' ')

    for i in range(1, N + 1):
        if not visited[i] and graph[vertex][i] == 1:
            dfs(i)


def bfs(vertex):
    queue = [vertex]
    visited[vertex] = False

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for i in range(1, N + 1):
            # dfs에서 visited가 모두 True가 됐으므로 bfs에서는 False로 방문 여부 확인
            if visited[i] and graph[vertex][i] == 1:
                queue.append(i)
                visited[i] = False


dfs(V)
print()
bfs(V)