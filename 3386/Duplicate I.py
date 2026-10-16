"""Dupe"""
def main():
    """main"""
    m = int(input())
    n = int(input())
    g1 = set()
    for _ in range(m):
        g1.add(int(input()))
    g2 = set()
    for _ in range(n):
        g2.add(int(input()))
    common = g1 & g2
    if not common:
        print("Nope")
    else:
        sorted_common = sorted(common, reverse=True)
        for i in sorted_common:
            print(i)
main()
