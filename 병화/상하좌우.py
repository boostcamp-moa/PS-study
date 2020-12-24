N = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            new_x = x + dx[i]
            new_y = y + dy[i]
    if new_x < 1 or new_y < 1 or new_x > N or new_y > N:
        continue
    x, y = new_x, new_y

print(x, y)