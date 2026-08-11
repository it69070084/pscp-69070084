"""point"""
number = int(input())
i = 0
score = 0
while i < number:
    op = input()
    match op:
        case "+":
            score += 10
        case "-":
            score -= 5
    i +=1
print(score)
