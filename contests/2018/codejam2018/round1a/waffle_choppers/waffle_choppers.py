

def fill_chips(grid, chips, r, c):
    for i in range(c+1):
        chips[0][i] = 0

    for j in range(r+1):
        chips[j][0] = 0

    for j in range(1, r+1):
        for i in range(1, c+1):
            chips[j][i] = grid[j-1][i-1] + chips[j-1][i] + chips[j][i-1] - chips[j-1][i-1]


def n_chips_in(chips, y0, x0, y1, x1):
    return chips[y1][x1] - chips[y0][x1] - chips[y1][x0] + chips[y0][x0]


def cut_h(grid, chips, r, c, h, v, v_cuts, h_cuts):
    if len(h_cuts) == h+1:
        return True

    n_chips = chips[r][c]
    n_chips_per_y = n_chips // (h+1)
    n_chips_per_dinner = n_chips // ((h+1)*(v+1))

    y0 = h_cuts[-1]
    for y in range(y0+1, r):
        y_chips = n_chips_in(chips, y0, 0, y, c)
        if y_chips > n_chips_per_y:
            break

        if y_chips == n_chips_per_y:
            ok = True
            x0 = v_cuts[0]
            for x in v_cuts[1:]:
                xy_chips = n_chips_in(chips, y0, x0, y, x)
                if xy_chips != n_chips_per_dinner:
                    ok = False
                    break

                x0 = x

            if ok and cut_h(grid, chips, r, c, h, v, v_cuts, h_cuts + [y]):
                return True

    return False


def cut_v(grid, chips, r, c, h, v, v_cuts):
    if len(v_cuts) == v+1:
        return cut_h(grid, chips, r, c, h, v, v_cuts, [0])

    n_chips = chips[r][c]
    n_chips_per_x = n_chips // (v+1)

    x0 = v_cuts[-1]
    for x in range(x0+1, c):
        x_chips = n_chips_in(chips, 0, x0, r, x)
        if x_chips > n_chips_per_x:
            break

        if x_chips == n_chips_per_x and cut_v(grid, chips, r, c, h, v, v_cuts + [x]):
            return True

    return False


def solve(grid, r, c, h, v):
    assert len(grid) == r
    assert 1 <= h < r
    assert 1 <= v < c

    n_chips = 0
    for row in grid:
        n_chips += sum(cell for cell in row if cell)

    if n_chips == 0:
        return True

    n_dinners = (h+1)*(v+1)
    if n_chips % n_dinners != 0:
        return False

    chips = [[0]*(c+1) for _ in range(r+1)]
    fill_chips(grid, chips, r, c)

    assert n_chips == chips[r][c]

    if h == v == 1:
        n_chips_per_dinner = n_chips // n_dinners
        for x in range(c):
            for y in range(r):
                c1 = n_chips_in(chips, 0, 0, y, x)
                c2 = n_chips_in(chips, y, x, r, c)
                c3 = n_chips_in(chips, 0, x, y, c)
                c4 = n_chips_in(chips, y, 0, r, x)
                if c1 == c2 == c3 == c4 == n_chips_per_dinner:
                    return True

        return False

    return cut_v(grid, chips, r, c, h, v, [0])


def main():
    for t in range(int(input())):
        r, c, h, v = tuple(int(w) for w in input().split())
        grid = []
        for i in range(r):
            grid.append(tuple((1 if ch == '@' else 0) for ch in input().strip()))

        r = solve(grid, r, c, h, v)
        if r:
            print("Case #{}: {}".format(t+1, 'POSSIBLE'))
        else:
            print("Case #{}: {}".format(t+1, 'IMPOSSIBLE'))

main()
