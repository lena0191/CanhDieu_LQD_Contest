n = int(input())
dem = 0
for i in range(2, n):
    if n % i == 0:
        dem += 1
print(dem)
