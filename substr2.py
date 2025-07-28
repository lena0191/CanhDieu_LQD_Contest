y = input()
N = int(input())

for _ in range(N):
    L, R = map(int, input().split())
    print(y[L:R])
