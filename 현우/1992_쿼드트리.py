import sys

n = int(input()) # 2의 제곱수
lst = [sys.stdin.readline().strip() for i in range(n)]
result = ''


def solution(x, y, n):
	global result

	if n == 2:
		tmp = ''
		for i in range(n):
			for j in range(n):
				tmp += lst[x+i][y+j]
		if len(set(tmp)) == 1:
			result += tmp[0]
			return
		result += ('(' + tmp + ')')
		return

	standard = lst[x][y]
	for i in range(n):
		for j in range(n):
			if lst[x+i][y+j] != standard:
				result += '('
				solution(x, y, n//2)
				solution(x, y + n//2, n//2)
				solution(x + n//2, y, n//2)
				solution(x + n//2, y + n//2, n//2)
				result += ')'
				return
	result += standard

solution(0, 0, n)
print(result)
