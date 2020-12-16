import random, time

def enqueue(queue, data):
    queue.append(data)

def dequeue(queue):
    if len(queue) == 0:
        print('Queue is Blank')

        return -1

    else:
        data = queue.pop(0)

        return data

def digit(d, k):
    temp = 1

    for i in range(1, k):
        temp *= 10

    d = d // temp
    d %= 10

    return d

def rs(b, n, m, queue):
    for k in range(1, m + 1):
        for i in range(1, n + 1):
            kd = digit(b[i], k)
            enqueue(queue[kd], a[i])

        p = 0

        for i in range(10):
            while len(queue[i]) != 0:
                p += 1

                a[p] = dequeue(queue[i])

def checkSort(b, n):
    isSorted = True

    for i in range(1, n):
        if (a[i] > a[i + 1]):
            isSorted = False

        if (not isSorted):
            break

    if isSorted:
        print('Sort Complete')

    else:
        print('Sort Error')

for number in range(100000, 400000, 100000):
    #a = [random.randrange(1, number) for i in range(number)] #랜덤
    #a = [i for i in range(number)] #정렬
    a = [i for i in range(number, 0, -1)]  # 역순

    Q = []

    for i in range(10):
        Q.append([])

    start_time = time.time()

    rs(a, len(a) - 1, 6, Q)
    #rs(a, N, M, Q), a = 배열, N = 원소의 개수, M = 자릿수

    end_time = time.time() - start_time

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)
    checkSort(a, len(a) - 1)
    print()