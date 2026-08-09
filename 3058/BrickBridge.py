'''brige'''
a = int(input())
b = int(input())
goal = int(input())
remain = goal - (b*5)
if remain < 0 :
    remain += (abs(remain) // 5) * 5
    if abs(remain) % 5:
        remain += 5
if remain > a :
    print(-1)
else:
    print(remain)
