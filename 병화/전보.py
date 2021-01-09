import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

v, e, start = map(int, input().split())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

city = 0
time = 0

for d in distance:
    if d != INF:
        city += 1
        time = max(time, d)

# 자기 자신 제외
print(city - 1, time)
