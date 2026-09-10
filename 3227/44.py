"""ไพ่ 44 ใบ"""
card = input().upper()
letter = {"A": "ace", "J": "jack", "Q": "queen", "K": "king"}
chanit = {"C": "clubs", "D": "diamonds", "H": "hearts", "S": "spades"}

if len(card) == 2:
    if card.startswith(tuple(letter.keys())):
        print(f"{letter[card[0]]} of {chanit[card[1]]}")
    else:
        print(f"{card[0]} of {chanit[card[1]]}")
elif len(card) == 3:
    print(f"{card[0:2]} of {chanit[card[2]]}")
