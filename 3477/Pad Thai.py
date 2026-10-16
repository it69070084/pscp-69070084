"""Pad Thai"""
def main():
    """main"""
    allowed_ingredients = {
        "Pad Thai Sauce",
        "Tofu",
        "Pickle Turnip",
        "Shrimp",
        "Bean Sprouts",
        "Noodle",
        "Chives",
        "Lime",
        "Egg",
        "Oil",
        "Peanuts",
    }

    required_tastes = {"Sweet", "Sour", "Salty"}

    ingredients = set()
    while True:
        line = input().strip()
        if line == "Cook":
            break
        if line:
            ingredients.add(line)

    tastes = set()
    while True:
        line = input().strip()
        if line == "End":
            break
        if line:
            tastes.add(line)

    for ing in ingredients:
        if ing not in allowed_ingredients:
            print("This is not Pad Thai!!!")
            return

    if not allowed_ingredients.issubset(ingredients):
        print("This is bad!")
        return

    if tastes == required_tastes:
        print("Delicious!")
    else:
        print("Not Bad...")
main()
