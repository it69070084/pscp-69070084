"""CuteCat CuteFox"""
def main():
    """main"""
    n_str = input()
    if not n_str.strip():
        return
    n = int(n_str.strip())


    animals = {}

    for _ in range(n):
        line = input().strip()
        if not line:
            continue
        cleaned = line.strip("{}").strip()
        parts = cleaned.split(":")
        if len(parts) == 2:
            key = parts[0].strip().strip('"').strip("'")
            val = parts[1].strip().strip('"').strip("'")
            animals[key] = val

    if "Garfield" not in animals and "Cat01" not in animals.values():
        animals["Garfield"] = "Cat01"
    if "Fubuki" not in animals and "Fox01" not in animals.values():
        animals["Fubuki"] = "Fox01"

    cats = {
        name: ident
        for name, ident in animals.items()
        if ident.lower().startswith("cat")
    }
    foxes = {
        name: ident
        for name, ident in animals.items()
        if ident.lower().startswith("fox")
    }

    def get_number(ident):
        digits = "".join(filter(str.isdigit, ident))
        return int(digits) if digits else 0

    print(f"Cat : {len(cats)}")
    print(f"Fox : {len(foxes)}")

    for name, ident in sorted(cats.items(), key=lambda x: get_number(x[1])):
        print(f"{name} : {ident}")

    for name, ident in sorted(foxes.items(), key=lambda x: get_number(x[1])):
        print(f"{name} : {ident}")

main()
