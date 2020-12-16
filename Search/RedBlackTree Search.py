black = 0
red = 1

class node:
    def __init__(self, color, key=None, left=None, right=None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right


class Dict:
    x = p = q = gg = node

    z = node(color=black, key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(color=black, key=0, left=0, right=z)

    def search(self, search_key):
        x = self.head.right

        while x != self.z:
            if x.key == search_key:
                return x.key

            if x.key > search_key:
                x = x.left

            else:
                x = x.right

        return -1

    def insert(self, v):
        x = p = g = self.head

        while x != self.z:
            gg = g
            g = p
            p = x

            if x.key == v:
                return

            if x.key > v:
                x = x.left

            else:
                x = x.right

            if x.left.color and x.right.color:
                self.split(x, p, g, gg, v)

        x = node(color=red, key=v, left=self.z, right=self.z)

        if p.key > v:
            p.left = x

        else:
            p.right = x

        self.split(x, p, g, gg, v)
        self.head.right.color = black

    def split(self, x, p, g, gg, v):
        x.color = red
        x.left.color = black
        x.right.color = black

        if p.color:
            g.color = red

            if g.key > v != p.key > v:
                p = self.rotate(v, g)

            x = self.rotate(v, gg)
            x.color = black

    def rotate(self, v, y):
        gc = c = node

        if y.key > v:
            c = y.left

        else:
            c = y.right

        if c.key > v:
            gc = c.left
            c.left = gc.right
            gc.right = c

        else:
            gc = c.right
            c.right = gc.left
            gc.left = c

        if y.key > v:
            y.left = gc

        else:
            y.right = gc

        return gc

    def check(self, n):
        print('===========================================')
        print(key)

        for i in range(1, n + 1):
            x = p = self.head

            while x != self.z:
                if x.key == i:
                    break

                if x.key > i:
                    p = x
                    x = x.left

                else:
                    p = x
                    x = x.right

            print('key : %3d parent : %3d color : ' % (x.key, p.key), end='')

            if x.color == black:
                print('black')

            else:
                print('red')

        print('===========================================')


import random, time

for N in range(1000, 4000, 1000):
    print('Start')

    key = list(range(1, N + 1))
    s_key = list(range(1, N + 1))
    parent = [-1 for i in range(N + 1)]
    random.shuffle(key)

    d = Dict()
    for i in range(N):
        d.insert(key[i])

    start_time = time.time()

    for i in range(N):
        result = d.search(s_key[i])

        if result == -1 or result != s_key[i]:
            print('Search Error!')

    end_time = time.time() - start_time

    d.check(N)

    print('Time (N = %d) : %f' % (N, end_time))
    print('End')
    print()
