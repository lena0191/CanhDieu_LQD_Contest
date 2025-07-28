a = list(map(int, input().split()))
b = []

for i in range(len(a)):
    if i % 2 == 0: 
        b.append(a[i] + 1)
    else:         
        b.append(a[i])

p = sum(1 for x in a if x % 2 == 0)
q = sum(1 for x in b if x % 2 == 0)

if p < q:
    print("a it hon")
elif p > q:
    print("b it hon")
else:
    print("Bang nhau")
