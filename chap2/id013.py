import math
n = int(input())

def print_divisor(n):
    for i in range(1, math.floor(n ** 0.5)+1):
        if n % i == 0:
            print(f"{i}\n{n // i}")

print_divisor(n)
