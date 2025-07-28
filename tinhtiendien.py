a, b, d1, d2, d3, x = map(int, input().split())
if x <= a:
    tong = x * d1
elif x <= b:
    tong = a * d1 + (x - a) * d2
else:
    tong = a * d1 + (b - a) * d2 + (x - b) * d3

print(total)
