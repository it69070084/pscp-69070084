"""pucci"""
start, stop = map(int, input().split())
ans = []

def is_prime(n):
    """isprime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True

for k in range(start, stop + 1):
    if is_prime(k):
        ans.append(k)

for l in ans:
    if l != ans[-1]:
        print(l,end=" ")
    else:
        print(l)

print("Total primes:", len(ans))
