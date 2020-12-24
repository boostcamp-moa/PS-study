N, M = map(int, input().split())
x, y, direction = map(int, input().split())
visited = [[0] * M for _ in range(N)]
visited[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maps = [list(map(int, input().split())) for _ in range(N)]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0

while True:
    turn_left()

    next_x = x + dx[direction]
    next_y = y + dy[direction]

    # 방문하지 않았고, 육지인 경우
    if visited[next_x][next_y] == 0 and maps[next_x][next_y] == 0:
        visited[next_x][next_y] = 1
        x = next_x
        y = next_y
        count += 1
        turn_time = 0
        continue
    # 방문했거나, 바다인 경우
    else:
        turn_time += 1

    # 4번 회전한 경우
    if turn_time == 4:
        next_x = x - dx[direction]
        next_y = y - dy[direction]

        # 뒤로 간 곳이 육지인 경우
        if maps[next_x][next_y] == 0:
            x = next_x
            y = next_y
        # 뒤로 간 곳이 바다인 경우
        else:
            break
        turn_time = 0

print(count)
