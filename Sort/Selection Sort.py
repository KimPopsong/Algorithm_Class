import random, time

a = []

def SelectionSort(b, n):
    for i in range(1, n):
        min = i

        for j in range(i + 1, n + 1):
            if(b[min] > b[j]):
                min = j

        b[i], b[min] = b[min], b[i]
        print(b)

    print(b)

for number in range(5000, 20000, 5000):
    #a = [random.randrange(1, number) for i in range(number)] #랜덤
    #a = [ i for i in range(number)] #정렬
    #a = [ i for i in range(number, 0, -1)] #역순
    a = [-1, 11, 15, 6, 2, 9, 8, 3, 1, 10, 13, 14, 5, 12, 4, 7]

    start_time = time.time()

    SelectionSort(a, len(a) - 1)

    end_time = time.time() - start_time

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)