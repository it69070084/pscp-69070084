"""short"""
def main():
    """short"""
    start = None
    end = None
    data = []
    while True:
        num = int(input())
        if num == -1:
            break
        if start is None:
            start = num
            end = num
        elif num == end + 1:
            end = num
        else:
            if start == end:
                data.append(str(start))
            else:
                data.append(f"{start}-{end}")
            start = num
            end = num
    if start is not None:
        if start == end:
            data.append(str(start))
        else:
            data.append(f"{start}-{end}")
    print(", ".join(data))
main()
