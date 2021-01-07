import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

v = int(input())
e = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    x, y, dist = map(int, input().split())
    graph[x].append((y, dist))


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


start, end = map(int, input().split())

dijkstra(start)

print(distance[end])