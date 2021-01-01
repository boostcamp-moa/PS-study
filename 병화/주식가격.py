# 이중 for문을 이용한 풀이

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        value = prices[i]
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if value > prices[j]:
                break

    return answer

# queue를 이용한 풀이

from collections import deque

def solution(prices):
    answer = []

    queue = deque(prices)

    while queue:
        price = queue.popleft()
        count = 0
        for num in queue:
            count += 1
            if price > num:
                break
        answer.append(count)

    return answer