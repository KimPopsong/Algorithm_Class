import geo as g

class rect:
    def __init__(self):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

def insideReact(p, t_range):
    t1 = p.x >= t_range.x1 and p.x <= t_range.x2
    t2 = p.y >= t_range.y1 and p.y <= t_range.y2

    return t1 and t2

class Range:
    dummy = g.point(0,0,None)

    class node:
        p = g.point
        l = None
        r = None

        def __init__(self, pp, ll ,rr):
            self.p = pp
            self.l= ll
            self.r = rr

    z = node(dummy, 0,0)
    z.l = z
    z.r = z
    head = node(dummy, 0, z)

    def insert(self, p):
        d = True
        f = self.node
        t = self.head

        while t != self.z:
            if d:
                td = p.x < t.p.x

            else:
                td = p.y < t.p.y

            f = t

            if td:
                t = t.l

            else:
                t = t.r

            d = not d

        t = self.node(self.dummy, 0 ,0)
        t.p = p
        t.l = self.z
        t.r = self.z

        if td:
            f.l = t

        else:
            f.r = t

    def search(self, t_range):
        return self.searchr(self.head.r, t_range, 0)

    def searchr(self,t,t_range,d):
        count = 0

        if t == self.z:
            return 0

        tx1 = t_range.x1 < t.p.x
        tx2 = t.p.x <= t_range.x2
        ty1 = t_range.y1 < t.p.y
        ty2 = t.p.y <= t_range.y2

        if d:
            t1 = tx1
            t2 = tx2

        else:
            t1 = ty1
            t2 = ty2

        if t1:
            count += self.searchr(t.l, t_range,  not d)

        if insideReact(t.p, t_range):
            count += 1

        if t2:
            count += self.searchr(t.r,t_range, not d)

        return count

N = 8
r = Range()
t_range = rect()
p = []

for i in range(N):
    p.append(g.point(g.x_value[i], g.y_value[i], g.c_value[i]))

for i in range(N):
    r.insert(p[i])

t_range.x1 = 3
t_range.y1 = 1
t_range.x2 = 7
t_range.y2 = 3

result = r.search(t_range)
print("범위 내에 있는 점의 개수 : ", result)