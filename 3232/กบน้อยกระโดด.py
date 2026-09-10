"""กบน้อยกระโดด"""
X,Y = map(int, input().split())
pos = 0
count = 0
while X > 0:
    count += 1
    pos += X
    if pos >= Y:
        break
    X -= 2
if pos >= Y:
    print(count)
else:
    print(-1)
