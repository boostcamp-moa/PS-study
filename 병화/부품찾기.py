# 이진 탐색 풀이
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())
stock = list(map(int, input().split()))
M = int(input())
order = list(map(int, input().split()))

for item in order:
    result = binary_search(stock, item, 0, N - 1)
    print('yes', end=' ') if result != None else print('no', end=' ')


# 계수 정렬 풀이
N = int(input())
stock = [0] * 1000001

for i in input().split():
    stock[int(i)] = 1

M = int(input())
order = list(map(int, input().split()))

for item in order:
    if stock[item] == 1:
        print('yes')
    else:
        print('no')


# 집합 이용 풀이
N = int(input())
stock = set(map(int, input().split()))

M = int(input())
order = list(map(int, input().split()))

for item in order:
    if item in stock:
        print('yes')
    else:
        print('no')
        