
def gcd(a, b):
    big, small = max(a, b), min(a, b)
    while small > 0:
        big, small = small, big % small
    return big

n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, n):
    tmp = gcd(ans, a[i])
    ans = ans * a[i] // tmp

print(ans)
