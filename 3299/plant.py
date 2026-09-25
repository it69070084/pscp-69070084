"""power plant"""
L, N = map(int, input().split())

k = 1
while True:
    total_cells = (k * L) * (k * L + 1) // 2
    if total_cells >= N:
        print(k)
        break
    k += 1
