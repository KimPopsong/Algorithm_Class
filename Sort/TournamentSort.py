import time, random

def TournamentSort(arr, n):
    length = n + 1
    count = 0
    b = []
    temp = []

    while(True):
        if(length <= 0):
            break

        length //= 2
        count += 1
    count += 1

    length = 1
    for i in range(0, count):
        length *= 2

    for i in range(0, length):
        b.append(0)

    for i in range(0, length // 2):
        b[i] = 0

        if(n >= i):
            b[(length // 2) + i] = arr[i]

    for k in range(0, n):
        for i in range(length - 1, 1, -2):
            if (b[i] > b[i - 1]):
                b[i // 2] = b[i]

            else:
                b[i // 2] = b[i - 1]

        temp.append(b[1])
        erase = b[1]

        for i in range(0, length, 1):
            if(b[i] == erase):
                b[i] = 0

    return temp

for number in range(1000, 4000, 1000):
    #a = [random.randrange(1, number) for i in range(number)] #랜덤
    #a = [i for i in range(number)] #정렬
    a = [i for i in range(number, 0, -1)]  # 역순

    start_time = time.time()

    a = TournamentSort(a, len(a) - 1)

    end_time = time.time() - start_time

    print(a)

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)