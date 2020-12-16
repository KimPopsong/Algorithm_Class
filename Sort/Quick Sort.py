import random, time
import sys
sys.setrecursionlimit(3002)

a = []

def qs(b, l, r):
    if(r > l):
        i = partition(b, l, r)
        print(b)
        qs(b, l, i - 1)
        print(b)
        qs(b, i + 1, r)
        print(b)

def partition(c, l, r):
    v = c[r]
    i = l - 1
    j = r

    while(1):
        while(1):
            i = i + 1

            if(c[i] >= v):
                break

        while(1):
            j = j - 1

            if(c[j] <= v):
                break

        if(i >= j):
            break

        c[i], c[j] = c[j], c[i]

    c[i], c[r] = c[r], c[i]

    return i

for number in range(1000, 4000, 1000):
    #a = [random.randrange(1, number) for i in range(number)] #랜덤
    #a = [i for i in range(number)] #정렬
    #a = [i for i in range(number, 0, -1)] #역순
    a = [-1, 11, 15, 6, 2, 9, 8, 3, 1, 10, 13, 14, 5, 12, 4, 7]

    start_time = time.time()

    qs(a, 1, len(a) - 1)

    end_time = time.time() - start_time

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)