import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
distance = [[INF] * m for _ in range(n)]

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0

    while q:
        x, y, cost = heapq.heappop(q)
        if x == n - 1 and y == m - 1:
            print(distance[n - 1][m - 1])
            return

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < m:
                new_cost = cost + graph[new_x][new_y]

                if new_cost < distance[new_x][new_y]:
                    distance[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_x, new_y, new_cost))

dijkstra()