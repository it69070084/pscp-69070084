"""store"""
num, check = map(int, input().split())

diff = [0] * 1442
i = 0

while i < num:
    start, stop = map(int, input().split())
    diff[start] += 1
    diff[stop] -= 1
    i += 1

open_count = [0] * 1441
current_open = 0

for t in range(1441):
    current_open += diff[t]
    open_count[t] = current_open

queries = list(map(int, input().split()))
results = [str(open_count[queries[i]]) for i in range(check)]

print(" ".join(results))
