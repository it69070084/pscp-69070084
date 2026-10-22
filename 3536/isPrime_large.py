"""prime"""
n = int(input())

if n < 2:
    print("NO")
elif n == 2:
    print("YES")
elif not n % 2:
    print("NO")
else:
    limit = int(n**0.5)
    is_prime = True
    for i in range(3, limit + 1, 2):
        if not n % i:
            is_prime = False
            break
    print("YES" if is_prime else "NO")
