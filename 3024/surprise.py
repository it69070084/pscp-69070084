'''surprise'''
total = float(input())
max_num = float(input())
remain = total - max_num
min_num = max(0.0, remain - max_num)
if (max_num - min_num) > 2 :
    print("Surprising")
else :
    print("Not surprising")
