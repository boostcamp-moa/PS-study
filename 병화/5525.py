N = int(input())
M = int(input())
S = input()

answer = 0
count = 0
index = 0

while index <= M - 3:
    if S[index] == 'I' and S[index + 1] == 'O' and S[index + 2] == 'I':
        count += 1
        if count == N:
            count -= 1
            answer += 1
        index += 1
    else:
        count = 0
    index += 1

print(answer)