n, W = map(int, input().split())
d = list(map(int, input().split()))

d.sort()
count = 0
total = 0

for size in d:
    if total + size <= W:
        total += size
        count += 1
    else:
        break

print(count)
