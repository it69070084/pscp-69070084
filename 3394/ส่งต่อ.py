"""songtor"""
def main():
    """solve"""
    fst = input().split()
    N = int(fst[0])
    S = int(fst[1])
    nxt = [0] * (N + 1)
    for i in range(1, N + 1):
        nxt[i] = int(input())
    visit = set()
    current = S
    while current and current not in visit:
        visit.add(current)
        current = nxt[current]
    print(len(visit))
main()
