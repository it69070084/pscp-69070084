'''temp'''
temp = float(input())
base_in = input()
base_out = input()
match base_in:
    case "F":
        match base_out:
            case "F":
                pass
            case "K":
                temp = (temp - 32) * (5 / 9) + 273.15
            case "R":
                temp = temp + 459.67
            case "C":
                temp = (temp - 32) / 1.8
    case "K":
        match base_out:
            case "F":
                temp = (temp - 273.15) * 1.8 + 32
            case "K":
                pass
            case "R":
                temp = temp * 1.8
            case "C":
                temp = temp - 273.15
    case "R":
        match base_out:
            case "F":
                temp = temp - 459.67
            case "K":
                temp = temp * (5 / 9)
            case "R":
                pass
            case "C":
                temp = (temp - 491.67) * (5 / 9)
    case "C":
        match base_out:
            case "F":
                temp = (temp * 1.8) + 32
            case "K":
                temp = temp + 273.15
            case "R":
                temp = (temp + 273.15) * (9 / 5)
            case "C":
                pass
print(f"{temp:.2f}")
