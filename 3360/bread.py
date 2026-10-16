"""bread"""
w, h, _, _ = map(int, input().split())
x_cut = list(map(int, input().split()))
y_cut = list(map(int, input().split()))

dx = []
prev = 0
for x in x_cut:
    dx.append(x - prev)
    prev = x
dx.append(w - prev)

dy = []
prev = 0
for y in y_cut:
    dy.append(y - prev)
    prev = y
dy.append(h - prev)

dx.sort(reverse=True)
dy.sort(reverse=True)

max1 = dx[0] * dy[0]

max2 = max(dx[0] * dy[1], dx[1] * dy[0])

print(f"{max1} {max2}")
