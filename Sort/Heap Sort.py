import random, time

a = []
c = a.copy()

def hs(b, n):
    for i in range(n // 2, 0, -1):
        heapify(a, i, n)
        print(b)

    for i in range(n - 1, 0, -1):
        print(b)
        b[1], b[i + 1] = b[i + 1], b[1]
        heapify(a, 1, i)

        print(b)

def heapify(b, h, m):
    v = b[h]

    j = 2 * h
    while(1):
        if(j > m):
            break

        if(j < m and b[j] < b[j + 1]):
            j = j + 1

        if(v >= b[j]):
            return

        else:
            b[j // 2] = b[j]

        j = 2 * j

    b[j //2] = v

for number in range(1000, 4000, 1000):
    #a = [random.randrange(1, number) for i in range(number)] #랜덤
    #a = [ i for i in range(number)] #정렬
    #a = [i for i in range(number, 0, -1)]  # 역순

    a = [11, 15, 6, 2, 9, 8, 3, 1, 10, 13, 14, 5, 12, 4, 7]

    c = a.copy()

    start_time = time.time()

    hs(a, len(a) - 1)

    end_time = time.time() - start_time

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)