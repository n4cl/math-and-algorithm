n = int(input())

def factorization(n):
    ans = []
    div = 2
    while div * div <= n:
        if n % div == 0:
            ans.append(str(div))
            n = n // div
        else:
            div += 1
    ans.append(str(n))
    print(" ".join(ans))

factorization(n)
