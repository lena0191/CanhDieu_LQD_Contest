import math

n, m = map(int, input().split())
pa, pb = map(int, input().split())

if m >= n:
    print(0)
else:
    daily = pa + pb
    need = n - m
    days = math.ceil(need / daily)
    print(days)
