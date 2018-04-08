import math
import sys


DEBUG = False
EPS = 1.E-8


def rotate_2d(x, y, cos_phi):
    sin_phi = math.sqrt(1 - cos_phi**2)
    x1 = x * cos_phi - y * sin_phi
    y1 = x * sin_phi + y * cos_phi

    if abs(x1) < EPS:
        x1 = 0

    if abs(y1) < EPS:
        y1 = 0

    return x1, y1


def rotate_z(points, cos_phi):
    res = []
    for p in points:
        x, y, z = p
        if x == y == 0:
            res.append(p)
        else:
            x1, y1 = rotate_2d(x, y, cos_phi)
            res.append((x1, y1, z))

    return res


def rotate_x(points, cos_phi):
    res = []
    for p in points:
        x, y, z = p
        if z == y == 0:
            res.append(p)
        else:
            y1, z1 = rotate_2d(y, z, cos_phi)
            res.append((x, y1, z1))

    return res


def project_xz(points):
    res = {(x,z) for (x, y, z) in points}
    return list(res)


def vect_sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def vect_mul(a, b):
    ax, ay = a
    bx, by = b
    return ax * by - ay * bx


def convex(points):
    if DEBUG and False:
        print("polygon:", points, file=sys.stderr)

    res = []
    points.sort()
    res.append(points.pop(0))
    while points:
        p0 = res[-1]
        k = -1
        p1 = res[0]
        for i in range(0, len(points)):
            p = points[i]
            u = vect_sub(p1, p0)
            v = vect_sub(p, p0)
            if vect_mul(u, v) >= 0.:
                k = i
                p1 = points[k]

        if k == -1:
            break

        res.append(p1)
        points.pop(k)

    res.append(res[0])

    if DEBUG and False:
        print("convex: ", res, file=sys.stderr)

    return res


def convex_square(points):
    tot_square = 0.
    p = points[0]
    for i in range(len(points)):
        p1 = points[i]
        x, y = p
        x1, y1 = p1
        square = (y + y1) * 0.5 * (x1 - x)
        tot_square += square
        p = p1

    return tot_square


def polygon_3d_square_xz(points):
    return convex_square(convex(project_xz(points)))


def find_theta(corners, a):
    theta0 = 0.
    theta1 = math.pi*0.25
    square0 = polygon_3d_square_xz(rotate_x(corners, math.cos(theta0)))
    square1 = polygon_3d_square_xz(rotate_x(corners, math.cos(theta1)))

    theta = (theta1 + theta0) * 0.5
    square = polygon_3d_square_xz(rotate_x(corners, math.cos(theta)))
    while abs(square1-square0) > EPS:

        if DEBUG:
            print("thetas:", theta0, theta, theta1, file=sys.stderr)
            print("squares:", square0, square, square1, file=sys.stderr)

        if square <= a:
            theta0 = theta
            square0 = square
        else:
            theta1 = theta
            square1 = square

        theta = (theta1 + theta0) * 0.5
        square = polygon_3d_square_xz(rotate_x(corners, math.cos(theta)))

    if DEBUG:
        print("square found:", square, file=sys.stderr)

    return theta


def solve(a):
    centers = ((0.5, 0, 0), (0, 0.5, 0), (0, 0, 0.5))
    corners = []
    for x in (-0.5, 0.5):
        for y in (-0.5, 0.5):
            for z in (-0.5, 0.5):
                corners.append((x, y, z))

    if a > math.sqrt(2):
        cos_alpha = math.cos(0)
    else:
        cos_alpha = a / math.sqrt(2)

    if DEBUG:
        print("cos_alpha:", cos_alpha, file=sys.stderr)

    cos_phi = math.sqrt(1 - cos_alpha**2) * math.sin(math.pi*0.25) + cos_alpha * math.cos(math.pi*0.25)

    centers = rotate_z(centers, cos_phi)
    corners = rotate_z(corners, cos_phi)
    square = polygon_3d_square_xz(corners)

    if DEBUG:
        print("z-rotation square:", square, file=sys.stderr)
        print("z-rotation centers:", centers, file=sys.stderr)

    if a > math.sqrt(2) and square + EPS < a:
        cos_theta = math.cos(find_theta(corners, a))
        centers = rotate_x(centers, cos_theta)
        corners = rotate_x(corners, cos_theta)
        square = polygon_3d_square_xz(corners)

        if DEBUG:
            print("x-rotation square:", square, file=sys.stderr)
            print("x-rotation centers:", centers, file=sys.stderr)

    return centers


def print_res(sol):
    for p in sol:
        x, y, z = p
        print("{} {} {}".format(x, y, z))


def main():
    for t in range(int(input())):
        a = float(input())
        sol = solve(a)
        if DEBUG:
            sys.stderr.flush()

        print("Case #{}:".format(t+1))
        print_res(sol)

main()
