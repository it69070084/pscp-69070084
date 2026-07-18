'''ink'''
import math
spd, house = map(int, input().split())
while house > 0:
    x, y = map(int, input().split())
    area = (pow(x,2) + pow(y,2)) * 3.1416
    print(math.ceil(area / spd))
    house -= 1
