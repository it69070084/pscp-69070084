'''castle'''
room = int(input())
remain, walls, row = room, 0, 0
while remain > 0:
    remain -= (row * 2 + 1)
    row += 1
walls = (row - 1) * 2 - (1 if (row % 2) != (room % 2) else 0)
print(walls)
