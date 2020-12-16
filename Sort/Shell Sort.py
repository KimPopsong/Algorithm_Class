import random, time

a = []

def ss(b, n):
    h = 1

    while h < n:
        h *= 3 + 1

    while h > 0:
        print(b)
        for i in range(h + 1, n + 1):
            b[0] = b[i]
            j = i

            while(j > h and b[j - h] > b[0]):
                print(b)
                b[j] = b[j - h]
                j -= h

            b[j] = b[0]

        h //= 3
    print(b)

for number in range(5000, 20000, 5000):
    #a = [random.randrange(1, number) for i in range(number)] #랜덤
    #a = [ i for i in range(number)] #정렬
    #a = [i for i in range(number, 0, -1)]  # 역순
    a = [-1, 11, 15, 6, 2, 9, 8, 3, 1, 10, 13, 14, 5, 12, 4, 7]

    start_time = time.time()

    ss(a, len(a) - 1)

    end_time = time.time() - start_time

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)