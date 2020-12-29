N = int(input())
maps = [list(map(int, input())) for _ in range(N)]


def divide(x, y, n):
    check = maps[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if maps[i][j] != check:
                print('(', end='')
                divide(x, y, n // 2)
                divide(x, y + n // 2, n // 2)
                divide(x + n // 2, y, n // 2)
                divide(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return
    if check == 0:
        print('0', end='')
    elif check == 1:
        print('1', end='')
    return

divide(0, 0, N)