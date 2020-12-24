from collections import deque
import sys
import re

n = int(sys.stdin.readline().strip())
answers = []

for i in range(n):
	func_list = sys.stdin.readline().strip()
	cnt = int(sys.stdin.readline().strip())
	lst_temp = sys.stdin.readline().strip()
	lst = [] if lst_temp == '[]' else list(map(int, lst_temp[1:-1].split(',')))

	if func_list.count('D') > cnt:
		answers.append('error')
		continue

	queue = deque(lst)
	direction = 0 # 0 : original, 1 : reversed

	for instruction in func_list:
		if instruction == 'R':
			direction = 1 if direction == 0 else 0
		elif instruction == 'D':
			if direction:
				queue.pop()
			else:
				queue.popleft()
	if direction:
		queue.reverse()

	answer = re.sub(' ', '', str(list(queue)))
	answers.append(answer)

for answer in answers:
	sys.stdout.write(answer+'\n')
