#!/Users/slava/work/fb_hacker_cup/venv/bin/python

import random

t = 1000

print(t)
for i in range(t):
    print(random.randint(5000, 10000), 10)
    buf = []
    for j in range(10):
        y = random.choice([10,12,20])
        x = random.randint(1, 20)
        z = random.randint(-5000, 5000)
        if z > 0:
            xdyz = '{}d{}+{}'.format(x,y,z)
        elif z < 0:
            xdyz = '{}d{}{}'.format(x,y,z)
        else:
            xdyz = '{}d{}'.format(x,y)
        buf.append(xdyz)

    print(' '.join(buf))



