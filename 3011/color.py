'''color'''
first = input()
second = input()
mixed_color = first+second
if "Red" in mixed_color and "Yellow" in mixed_color:
    print("Orange")
elif "Red" in mixed_color and "Blue" in mixed_color:
    print("Violet")
elif "Yellow" in mixed_color and "Blue" in mixed_color:
    print("Green")
elif first == "Red" and second == "Red":
    print("Red")
elif first == "Blue" and second == "Blue":
    print("Blue")
elif first == "Yellow" and second == "Yellow":
    print("Yellow")
else:
    print("Error")
