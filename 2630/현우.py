n = int(input())
lst = []
for i in range(n):
	lst.append([int(x) for x in input().split(' ')])

white_cnt = 0 # 흰색은 0
blue_cnt = 0 # 파란색은 1

def search(start_x, end_x, start_y, end_y):
	global white_cnt
	global blue_cnt

	color = -1
	for i in range(start_y, end_y + 1):
		target = lst[i][start_x : end_x +1]
		if len(set(target)) == 1:
			if color == -1: # 아직 color가 정해지지 않았을 때
				color = target[0]
			else: # color가 정해졌을 때
				if color != target[0]: # 다음 발견된 행이 이미 정해진 color와 다를 경우
					break
		else:
			break
	else:
		if color == 0:
			white_cnt += 1
		elif color == 1:
			blue_cnt += 1
		return

	search(start_x, start_x+((end_x-start_x)//2), start_y, start_y+((end_y-start_y)//2)) # 좌상단
	search(start_x+((end_x-start_x)//2)+1, end_x, start_y, start_y+((end_y-start_y)//2)) # 우상단
	search(start_x, start_x+((end_x-start_x)//2), start_y+((end_y-start_y)//2)+1, end_y) # 좌하단
	search(start_x+((end_x-start_x)//2)+1, end_x, start_y+((end_y-start_y)//2)+1, end_y) # 우하단

search(0, n-1, 0, n-1) # 시작 y, 끝 y, 시작 x, 끝 x
print(white_cnt)
print(blue_cnt)
