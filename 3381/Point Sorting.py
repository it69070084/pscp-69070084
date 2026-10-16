"""point"""
def main():
    """main"""
    lst = []
    def get_lst():
        """list"""
        while not lst:
            lst.extend(input().split()[::-1])
        return lst.pop()
    T = int(get_lst())
    for _ in range(T):
        N = int(get_lst())
        point = []
        for _ in range(N):
            x = int(get_lst())
            y = int(get_lst())
            point.append((x, y))
        def custom_key(p):
            """key"""
            return (p[0] + p[1], -p[1])
        point.sort(key=custom_key)
        for x, y in point:
            print(x, y)
main()
