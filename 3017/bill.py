'''bill'''
money = int(input())
tax = money * 0.1
if tax < 50:
    tax = 50
elif tax > 1000:
    tax = 1000
vat = (money + tax) + ((money + tax) * 0.07)
print(f"{vat:.02f}")
