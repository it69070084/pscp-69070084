"""GRaft"""
inp = int(input())
height = [int(input()) for _ in range(inp)]
if inp == 1:
    print(1)
else:
    count = 0
    for i in range(inp):
        if not i:
            if height[0] > height[1]:
                count += 1
        elif i == inp - 1:
            if height[inp - 1] > height[inp - 2]:
                count += 1
        else:
            if height[i] > height[i - 1] and height[i] > height[i + 1]:
                count += 1
    print(count)
