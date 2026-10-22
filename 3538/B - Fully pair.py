"""pair"""
def main():
    """main"""
    s = input().strip()
    if not s:
        return
    counts = {}
    seen = []
    for char in s:
        if char not in counts:
            seen.append(char)
            counts[char] = 0
        counts[char] += 1
    unpaired = [char for char in seen if counts[char] % 2]
    if unpaired:
        print("".join(unpaired))
    else:
        print("fully paired")
main()
