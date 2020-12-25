def solution(start, end):
	global n, r, c

	if n == 1:
		lst = [i for i in range(start, end+1)]
		result = lst[2*r + c]
		print(result)
		return
	else:
		step = pow(4, n - 1)
		if (r >= 0 and r < pow(2, n-1)) and (c >= 0 and c < pow(2, n-1)): # 좌상
			n -= 1
			solution(start + step * 0, start + step * 1 - 1)
		elif (r >= 0 and r < pow(2, n-1)) and (c >= pow(2, n-1) and c < pow(2, n)): # 우상
			n -= 1
			c -= pow(2, n)
			solution(start + step * 1, start + step * 2 - 1)
		elif (r >= pow(2, n-1) and r < pow(2, n)) and (c >= 0 and c < pow(2, n-1)): # 좌하
			n -= 1
			r -= pow(2, n)
			solution(start + step * 2, start + step * 3 - 1)
		elif (r >= pow(2, n-1) and r < pow(2, n)) and (c >= pow(2, n-1) and c < pow(2, n)): # 우하
			n -= 1
			r -= pow(2, n)
			c -= pow(2, n)
			solution(start + step * 3, start + step * 4 - 1)

n, r, c = map(int, input().split())
solution(0, pow(4, n) - 1)
