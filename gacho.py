n, m = map(int, input().split())
for ga in range(n + 1):
    cho = n - ga
    if 2 * ga + 4 * cho == m:
        print(ga, cho)
        break
