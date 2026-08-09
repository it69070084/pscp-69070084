"""sara"""
sara = {"a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0}
WORD = input().lower()
for i in WORD:
    if i in sara:
        sara[i] += 1
for KEY, count in sara.items():
    if count :
        print(KEY,":",count)
