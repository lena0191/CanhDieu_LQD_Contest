B = input().strip()
A = input().strip()
count = 0
i = 0
while i <= len(B) - len(A):
    if B[i:i+len(A)] == A:
        count += 1
        i += len(A)
    else:
        i += 1
print(count)
