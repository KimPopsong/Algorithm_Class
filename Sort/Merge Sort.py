import random, time

a = []
c = a.copy()

def ms(b, l, r):
    if(r > l):
        m = (r + l) // 2
        ms(b, l, m)
        ms(b, m + 1, r)
        merge(b, l, m, r)

def merge(b, l, m, r):
    i = l
    j = m + 1
    k = l

    while (i <= m and j <= r):
        if(b[i] < b[j]):
            c[k] = b[i]
            k = k + 1
            i = i + 1

        else:
            c[k] = b[j]
            k = k + 1
            j = j + 1

    if(i < m):
        for p in range(j, r + 1):
            c[k] = a[p]
            k = k + 1

    else:
        for p in range(i, m + 1):
            c[k] = b[p]
            k = k + 1

    for p in range(l, r + 1):
        b[p] = c[p]

def checkSort(a, n):
    isSorted = True

    for i in range(1, n):
        if(a[i] > a[i + 1]):
            isSorted = False

        if(not isSorted):
            break

    if isSorted:
        print("Sort Complete")

    else:
        print("Sort Error")

for number in range(100000, 400000, 100000):
    #a = [random.randrange(1, number) for i in range(number)] #랜덤
    a = [i for i in range(number)] #정렬
    #a = [i for i in range(number, 0, -1)]  # 역순

    c = a.copy()

    start_time = time.time()

    ms(a, 1, len(a) - 1)

    end_time = time.time() - start_time

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)