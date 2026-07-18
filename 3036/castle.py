'''castle'''
room = int(input())
remain = room
walls = 0
row = 0
odd_room = room % 2
for i in range(room):
    remain -= ((i * 2) +1)
    row += 1
    if remain <= 0 :
        walls = i * 2
        if row % 2 != odd_room :
            walls -= 1
        break
print(walls)
