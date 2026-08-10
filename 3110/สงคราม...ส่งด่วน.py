"""com"""
START, STOP = input().split()
weight = float(input())
match START,STOP:
    case "BKK", "CNX":
        print(f"{ 30 * weight + 10:.2f}")
    case "CNX", "UBP":
        print(f"{ 40 * weight + 15:.2f}")
    case "UBP", "BKK":
        print(f"{ 40 * weight + 20:.2f}")
    case "BKK", "PKT":
        print(f"{ 50 * weight + 25:.2f}")
    case "PKT", "CNX":
        print(f"{ 60 * weight + 30:.2f}")
    case "UBP", "PKT":
        print(f"{ 70 * weight + 40:.2f}")
    case _:
        print("Error")
