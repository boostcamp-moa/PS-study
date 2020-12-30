from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            # 지도 범위를 넘어가는 경우
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue
            # 괴물이 있는 부분
            if graph[new_x][new_y] == 0:
                continue
            # 괴물이 없는 부분
            if graph[new_x][new_y] == 1:
                graph[new_x][new_y] = graph[x][y] + 1
                queue.append((new_x, new_y))

    return graph[N - 1][M - 1]


print(bfs(0, 0))
