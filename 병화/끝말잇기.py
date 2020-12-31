N = int(input())
strings = list(input().split(' '))
alphabet = set()

for string in strings:
    alphabet.add(string[0])

print(1) if len(alphabet) == 1 else print(0)