"""สลากกินแบ่ง"""
huay_alp, huay_num = map(str, input().split())
lottary_alp, lottary_num = map(str, input().split())

if huay_alp == lottary_alp and huay_num == lottary_num:
    print(1000000)
elif huay_num == lottary_num:
    print(100000)
elif huay_alp == lottary_alp and huay_num[2:5] == lottary_num[2:5]:
    print(2000)
elif huay_alp == lottary_alp and huay_num[3:5] == lottary_num[3:5]:
    print(1000)
elif huay_num[2:5] == lottary_num[2:5]:
    print(200)
elif huay_num[3:5] == lottary_num[3:5]:
    print(100)
elif huay_alp == lottary_alp:
    print(20)
else:
    print(0)
