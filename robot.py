commands = input().strip()

x, y = 0, 0

for c in commands:
    if c == 'E':
        x += 1
    elif c == 'W':
        x -= 1
    elif c == 'N':
        y += 1
    elif c == 'S':
        y -= 1

print(x, y)
