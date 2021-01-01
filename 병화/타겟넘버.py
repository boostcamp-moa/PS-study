answer = 0


def dfs(index, sum, numbers, target):
    global answer
    if index == len(numbers):
        if sum == target:
            answer += 1
        return

    dfs(index + 1, sum + numbers[index], numbers, target)
    dfs(index + 1, sum - numbers[index], numbers, target)


def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)

    return answer