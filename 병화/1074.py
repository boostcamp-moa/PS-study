import sys
input = sys.stdin.readline


def recursion(start_row, end_row, start_col, end_col, n):
    # 출력 조건
    if X == start_row and Y == start_col:
        print(n)
        return

    # 4등분하기 위한 행의 경계값
    mid_row = (start_row + end_row) // 2
    # 4등분하기 위한 열의 경계값
    mid_col = (start_col + end_col) // 2

    # 4등분된 사각형의 크기
    N = (mid_row - start_row) * (mid_col - start_col)

    # 왼쪽 위
    if start_row <= X < mid_row and start_col <= Y < mid_col:
        recursion(start_row, mid_row, start_col, mid_col, n)
    # 오른쪽 위
    elif start_row <= X < mid_row and mid_col <= Y < end_col:
        recursion(start_row, mid_row, mid_col, end_col, n + N)
    # 왼쪽 아래
    elif mid_row <= X < end_row and start_col <= Y < mid_col:
        recursion(mid_row, end_row, start_col, mid_col, n + 2 * N)
    # 오른쪽 아래
    elif mid_row <= X < end_row and mid_col <= Y < end_col:
        recursion(mid_row, end_row, mid_col, end_col, n + 3 * N)


N, X, Y = map(int, input().split())
recursion(0, 2**N, 0, 2**N, 0)
