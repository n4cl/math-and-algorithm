n = int(input())
ans = []
for i in range(2, n+1):
    is_p = True
    for j in range(2, i):
        if (i % j) == 0:
            is_p = False
    if is_p:
        ans.append(str(i))
print(" ".join(ans))
