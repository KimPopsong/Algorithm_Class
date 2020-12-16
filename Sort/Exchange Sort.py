import random, time

a = []

def ExchangeSort(b, n):
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if(b[i] < b[j]):
                b[i], b[j] = b[j], b[i]

    print(b)

for number in range(5000, 20000, 5000):
    #a = [random.randrange(1, number) for i in range(number)] #랜덤
    a = [i for i in range(number)] #정렬
    #a = [i for i in range(number, 0, -1)] #역순

    start_time = time.time()

    ExchangeSort(a, len(a) - 1)

    end_time = time.time() - start_time

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)