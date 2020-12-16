import random, time

class node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Dict:
    def __init__(self):
        self.node = None
        self.height = 0
        self.balance = 0

    def search(self, searchKey):
        x = self.node
        while x is not None:
            if x.key == searchKey:
                return searchKey
            if x.key > searchKey:
                x = x.left.node
            else:
                x = x.right.node
        return -1

    def insert(self, v):
        x = self.node
        if x is None:
            self.node = node(v)
            self.node.left = Dict()
            self.node.right = Dict()

        elif x.key > v:
            self.node.left.insert(v)

        else:
            self.node.right.insert(v)

        self.checkBalance()

    def checkBalance(self):
        self.updateHeight(False)
        self.updateBalance(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotateLeft()
                self.rotateRight()

            else:
                if self.node.right.balance > 0:
                    self.node.right.rotateRight()
                self.rotateLeft()

            self.updateHeight()
            self.updateBalance()

    def rotateRight(self):
        g = self.node
        p = g.left.node
        x = p.right.node

        self.node = p
        p.right.node = g
        g.left.node = x

    def rotateLeft(self):
        g = self.node
        p = g.right.node
        x = p.left.node

        self.node = p
        p.left.node = g
        g.right.node = x

    def updateHeight(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.updateHeight()
                if self.node.right is not None:
                    self.node.right.updateHeight()
            self.height=max(self.node.left.height, self.node.right.height) + 1

        else:
            self.height = 0

    def updateBalance(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.updateBalance()
                if self.node.right is not None:
                    self.node.right.updateBalance()
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def check(self, n):
        print('=================================')
        print(key)

        for i in range(1, n + 1):
            x = self.node
            while x is not None:
                if x.key == i:
                    break
                if x.key > i:
                    p = x
                    x = x.left.node
                else:
                    p = x
                    x = x.right.node

            print('key : %d , parent : %d' %(x.key, p.key))

        print('=================================')

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