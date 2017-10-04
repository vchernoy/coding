# Enter your code here. Read input from STDIN. Print output to STDOUT
import random


def game(l,r,k):
    if r >= k:
        return True

    k_ = k - 1

    t = (k_) % (l + r)

    return t < r


def game0(l,r,k, s, tab):
    if s >= k:
        return False

    if s in tab:
        return tab[s]

    for step in range(r, l-1, -1):
        won = game0(l,r,k,s+step,tab)
        if not won:
            tab[s] = True
            return True

    tab[s] = False
    return False


def input_data():
    g = int(input())
    games = []
    for _ in range(g):
        l, r, k = [int(w) for w in input().split()]
        games.append((l,r,k))

    for l,r,k in games:
        tab = {}
        res = game(l,r,k)
        print('Alice' if res else 'Bob')
        res = game0(l,r,k, 0, tab)
        print('Alice' if res else 'Bob')
        print()


MAX = 10*6
for j in range(1000):
    l = random.randint(1, MAX)
    r = random.randint(l, MAX)
    k = random.randint(1, MAX*10)
    #k = j+1
    tab = {}
    win0 = game0(l, r, k, 0, tab)
    win1 = game(l,r,k)

    if win0 != win1:
        print(l, r, k, win0, win1)