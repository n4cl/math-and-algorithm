import math
n = int(input())

def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

print("Yes" if is_prime(n) else "No")
