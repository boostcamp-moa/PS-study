buttons = {str(i) for i in range(0, 10)}
target = int(input())
broken_num = int(input())
if broken_num:
	buttons = buttons - set(input().split())

result = target - 100 if target >= 100 else 100 - target

for channel in range(1000001):
	for num in str(channel):
		if num not in buttons:
			break
	else:
		result = min(result, len(str(channel)) + abs(target - channel))
print(result)
