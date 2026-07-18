'''mod10'''
NUMBER = str(input())
for i in range (int(NUMBER),0,-1):
    if (str(i))[-1] == "0":
        print(i,end=" ")
print(0)
