a, b = map(int, input().split())

def gcd(a, b):
    big, small = max(a, b), min(a, b)
    while small > 0:
        big, small = small, big % small
    return big

print(gcd(a, b))
