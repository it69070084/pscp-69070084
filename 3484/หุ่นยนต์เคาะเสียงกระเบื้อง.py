"""kraberng"""
def read():
    """input"""
    first_line = input().split()
    N = int(first_line[0])
    P = float(first_line[1])
    grid = []
    for _ in range(N):
        row = [int(x) for x in input().split()]
        grid.append(row)
    return N, P, grid

def rows(grid):
    """row"""
    total_def = 0
    total_pts = 0
    for row in grid:
        def_in_row = 0
        for x in row:
            if x > 0:
                def_in_row += 1
        pts_in_row = sum(row)
        total_def += def_in_row
        total_pts += pts_in_row
        print(*(row + [def_in_row, pts_in_row]))
    return total_def, total_pts

def cols(n, grid):
    """col"""
    col_defs = []
    col_pts = []
    for j in range(n):
        col_def = 0
        col_pts_sum = 0
        for i in range(n):
            if grid[i][j] > 0:
                col_def += 1
            col_pts_sum += grid[i][j]
        col_defs.append(col_def)
        col_pts.append(col_pts_sum)
    print(*col_defs)
    print(*col_pts)

def main():
    """main"""
    N, P, grid = read()
    total_def, total_pts = rows(grid)
    cols(N, grid)
    total_penalty = total_pts * P
    print(f"{total_def} {total_pts} {total_penalty:.2f}")

main()
