"""gift"""
N, K, T = map(int, input().split())
check = 0
gift = 1
while True :
    check += 1
    if gift == T:
        break
    if gift + K > N:
        gift = gift + K - N
    else:
        gift += K
    if gift == 1:
        break
print(check)
