# from collections import deque
# T = int(input())
#
# for _ in range(T):
#     # 입력
#     p = list(input())
#     n = int(input())
#     array = input()
#     if array != '[]':
#         array = list(map(int, array[1:-1].split(',')))
#
#     # 에러 검사
#     if p.count('D') > n:
#         print('error')
#         continue
#
#     # 함수 수행
#     queue = deque(array)
#     for func in p:
#         if func == 'D':
#             queue.popleft()
#         elif func == 'R':
#             queue.reverse()
#
#     print(list(queue))
#

import sys
T = int(sys.stdin.readline())

for _ in range(T):
    # 입력
    p = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    array = sys.stdin.readline().strip()
    if array != '[]':
        array = list(array[1:-1].split(','))

    # 함수 수행
    r_count = 0
    left, right = 0, 0

    for func in p:
        if func == 'R':
            r_count += 1
        elif func == 'D':
            if r_count % 2 == 0:
                left += 1
            else:
                right += 1

    if left + right <= n:
        array = array[left:n - right]
        if r_count % 2 == 0:
            print(f'[{",".join(array)}]')
        else:
            print(f'[{",".join(array[::-1])}]')
    else:
        print('error')