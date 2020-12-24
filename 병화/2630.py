N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0


def divide(x, y, n):
    global white, blue
    # 기준이 되는 첫 색깔
    check = maps[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 하나라도 색깔이 다른 경우
            if maps[i][j] != check:
                divide(x, y, n // 2)
                divide(x, y + n // 2, n // 2)
                divide(x + n // 2, y, n // 2)
                divide(x + n // 2, y + n // 2, n // 2)
                return
    # 모두 하얀색일 경우
    if check == 0:
        white += 1
    # 모두 파란색일 경우
    elif check == 1:
        blue += 1

divide(0, 0, N)
print(white)
print(blue)