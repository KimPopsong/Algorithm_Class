import random, time

a = []

def cs(b, n, m):
    c = [0] * (n + 1)
    count = [0] * (m + 1)

    for j in range(1, m + 1):
        count[j] = 0

    for i in range(1, n + 1):
        count[b[i]] += 1

    for j in range(2, m + 1):
        count[j] += count[j - 1]

    for i in range(n, 0, -1):
        c[count[b[i]]] = b[i]
        count[b[i]] -= 1

    for i in range(1, n + 1):
        b[i] = c[i]

for number in range(100000, 400000, 100000):
    N = number
    M = number

    a = [random.randrange(1, M) for i in range(N)] #랜덤
    #a = [ i for i in range(number)] #정렬
    #a = [i for i in range(number, 0, -1)]  # 역순

    start_time = time.time()

    cs(a, len(a) - 1, M)

    end_time = time.time() - start_time

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)