import sys
import math

DEBUG = False
W = H = 1000


def query(row, col):
    print(row, col)
    sys.stdout.flush()
    y, x = [int(w) for w in input().split()]
    return y, x


def dim(a):
    w1 = int(math.sqrt(a))
    h1 = (a + w1 - 1) // w1
    found_wh = []
    for h0 in range(w1, h1+1):
        for w0 in range(h0, h1+1):
            a0 = w0 * h0
            if a0 >= a:
                found_wh.append((w0, h0, a0))

    min_a0 = found_wh[0][2]
    found_wh = [t for t in found_wh if t[2] == min_a0]
    found_ww = [t for t in found_wh if t[0] == t[1]]
    if found_ww:
        return found_ww[0][0], found_ww[0][1]

    return found_wh[0][0], found_wh[0][1]


class Block:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.filled = 0

    def inc(self):
        self.filled += 1
        assert(self.filled <= 9)

    def __repr__(self):
        return "({},{}:{})".format(self.col, self.row, self.filled)

    def loc(self):
        return self.col, self.row


def block_at(x, y, grid, grid_blocks, all_blocks):
    b = grid_blocks[y][x]
    if b is None:
        b = Block(x, y)
        grid_blocks[y][x] = b
        for c in range(x-1, x+2):
            for r in range(y-1, y+2):
                if grid[r][c]:
                    b.inc()

        all_blocks[b.filled][(x, y)] = b

    return b


def build_blocks(grid, grid_blocks, x0, y0, w, h, all_blocks):
    for x in range(x0+1, x0+w-1):
        for y in range(y0+1, y0+h-1):
            _ = block_at(x, y, grid, grid_blocks, all_blocks)


def find_closest(blocks, cx, cy):
    best_b = None
    best_d = W*H
    for b in blocks.values():
        d = (b.col-cx)**2 + (b.row-cy)**2
        if d <= best_d:
            best_b = b
            best_d = d

    return best_b


def run(a):
    w, h = dim(a)
    assert(w * h >= a)

    grid = tuple([False] * W for _ in range(H))
    grid_blocks = tuple([None for _ in range(W)] for _ in range(H))
    all_blocks = tuple(dict() for _ in range(10))
    build_blocks(grid, grid_blocks, (W-w)//2, (H-h)//2, w, h, all_blocks)

    n_points = 0
    tot_x_points = tot_y_points = 0
    cx, cy = find_closest(all_blocks[0], W // 2, H // 2).loc()

    iterations = 0
    while iterations < 1000:
        least_filled_blocks_id = 0
        while least_filled_blocks_id < len(all_blocks) and not all_blocks[least_filled_blocks_id]:
            least_filled_blocks_id += 1

        if least_filled_blocks_id >= len(all_blocks):
            break

        b = find_closest(all_blocks[least_filled_blocks_id], cx, cy)
        iterations += 1
        prepared_row, prepared_col = query(b.row, b.col)
        if prepared_col <= 0 or prepared_row <= 0:
            break

        if not grid[prepared_row][prepared_col]:
            for r in range(prepared_row-1, prepared_row+2):
                for c in range(prepared_col-1, prepared_col+2):
                    b = grid_blocks[r][c]
                    if b is not None:
                        del all_blocks[b.filled][b.loc()]
                        b.inc()
                        all_blocks[b.filled][b.loc()] = b

            grid[prepared_row][prepared_col] = True
            n_points += 1
            tot_x_points += prepared_col
            tot_y_points += prepared_row
            cx = tot_x_points // n_points
            cy = tot_y_points // n_points

            if DEBUG:
                print("n_points:", n_points, file=sys.stderr)
                print("blocks:", [set(blocks.values()) for blocks in all_blocks], file=sys.stderr)
                print("iterations:", iterations, file=sys.stderr)

    if DEBUG:
        for prepared_row in range((H-h)//2-1, (H+h+1)//2+1):
            print(''.join([('+' if bit else '.') for bit in grid[prepared_row][(W-w)//2-1:(W+w)//2+1]]), file=sys.stderr)

    return iterations


def main():
    for t in range(int(input())):
        a = int(input())
        _ = run(a)

main()
