N = int(input())
M = int(input())
if M == 0:
    broken_buttons = []
else:
    broken_buttons = list(input().split())

# + 혹은 - 로 이동하는 경우(최대)
answer = abs(N - 100)

# num의 모든 자릿수에 대해 고장난 버튼에 포함되는지 확인
def check(num):
    for i in list(str(num)):
        if i in broken_buttons:
            return False
    return True

for num in range(1000001):
    if check(num):
        # len(str(num)) : 숫자를 누른 횟수
        # abs(N - num) : +/-를 누른 횟수
        answer = min(answer, len(str(num)) + abs(N - num))

print(answer)
