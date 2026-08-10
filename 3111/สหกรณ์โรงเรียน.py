"""sahagon"""
import math
MEMBER = input()
order = int(input())
price = 0
i = 0

while i < order:
    price += float(input())
    i += 1

match MEMBER:
    case "Y":
        price -= price * 0.05
    case "N":
        if price >= 500:
            price -= price * 0.03

price = math.ceil(price * 100) / 100

print(f"{price:.2f}")
