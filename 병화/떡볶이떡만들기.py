N, M = map(int, input().split())
array = list(map(int, input().split()))

array.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 10 15 17 19
        result = 0
        for item in array:
            diff = item - mid
            if diff > 0:
                result += diff
        if result == target:
            return mid
        elif result > target:
            start = mid + 1
        else:
            end = mid - 1
    return None


print(binary_search(array, M, 0, max(array)))
