#!/Users/slava/work/fb_hacker_cup/venv/bin/python

import fileinput, sys


def are_in_square(points, r, x, y):
    k = points[0]
    maxx = minx = x[k]
    maxy = miny = y[k]
    for k in points:
        maxx = max(maxx, x[k])
        minx = min(minx, x[k])
        maxy = max(maxy, y[k])
        miny = min(miny, y[k])

        if maxx - minx > r:
            return False

        if maxy - miny > r:
            return False

    return True


def minmax(points, x):
    k = points[0]
    maxx = minx = x[k]
    for k in points:
        maxx = max(maxx, x[k])
        minx = min(minx, x[k])

    return minx, maxx


def move(x, y, cx, cy, radius, dx, dy):
    n = len(x)
    x1 = list(x)
    y1 = list(y)

    radius_2 = radius**2
    for i in range(n):
        dist_2 = (cx - x[i])**2 + (cy - y[i])**2
        if dist_2 <= radius_2:
            x1[i] = x[i] + dx
            y1[i] = y[i] + dy

    return x1, y1


def move_destroy(g1, g2, x, y, r):
    minx1, maxx1 = minmax(g1, x)
    miny1, maxy1 = minmax(g1, y)
    cx1, cy1 = (maxx1 + minx1) / 2, (maxy1 + miny1) / 2
    radius = max(maxx1 - minx1, maxy1 - miny1)

    minx2, maxx2 = minmax(g2, x)
    miny2, maxy2 = minmax(g2, y)
    cx2, cy2 = (maxx2 + minx2) / 2, (maxy2 + miny2) / 2

    dx = cx2 - cx1
    dy = cy2 - cy1

    moved_x, moved_y = move(x, y, cx1, cy1, radius, dx, dy)

    points = mk_points(minx2, miny2, r, moved_x, moved_y)
    #new_groups = mk_groups(moved_x, moved_y, r)
    #return len(new_groups[0])

    return len(points)


def mk_points(x0, y0, r, x, y):
    n = len(x)

    x1 = x0 + r
    y1 = y0 + r
    points = ()
    for i in range(n):
        xi = x[i]
        yi = y[i]
        if x0 <= xi <= x1 and y0 <= yi <= y1:
            points = points + (i,)

    return points


def mk_groups(x, y, r):
    n = len(x)

    x_coords = sorted(x)
    y_coords = sorted(y)
    all_groups = [set() for _ in range(n+1)]
    for x0 in x_coords:
        for y0 in y_coords:
            points = mk_points(x0, y0, r, x, y)
            if points:
                n_points = len(points)
                all_groups[n_points].add(points)

    ordered_groups = []
    for groups in reversed(all_groups):
        for points in groups:
            ordered_groups.append(points)

    return ordered_groups


def fight(x, y, r):
    ordered_groups = mk_groups(x, y, r)

    #print(ordered_groups, file=sys.stderr)

    res = len(ordered_groups[0])
    m = len(ordered_groups)
    for i in range(m):
        if i > 0:
            max_res_ij = len(ordered_groups[i]) + len(ordered_groups[0])
            if max_res_ij <= res:
                break
        elif m >= 2:
            max_res_ij = len(ordered_groups[i]) + len(ordered_groups[1])
            if max_res_ij <= res:
                break

        for j in range(m):
            if i != j:
                max_res_ij = len(ordered_groups[i]) + len(ordered_groups[j])
                if max_res_ij <= res:
                    break

                res0 = move_destroy(ordered_groups[i], ordered_groups[j], x, y, r)
                res = max(res, res0)

    return res


def main():
    f = fileinput.input()

    for test in range(int(f.readline())):
        n, r = [int(w) for w in f.readline().split()]
        x = [0] * n
        y = [0] * n
        for i in range(n):
            xi, yi = [int(w) for w in f.readline().split()]
            x[i] = xi
            y[i] = yi

        res = fight(x, y, r)
        print('Case #{}: {}'.format(test+1, res))


main()


