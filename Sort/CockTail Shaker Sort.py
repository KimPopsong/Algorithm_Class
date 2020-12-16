import random, time

a = []

def CocktailShakerSort(b, n):
    left = 1
    right = n

    while(left < right):
        for i in range(left, right):
            if(b[i] > b[i + 1]):
                b[i], b[i + 1] = b[i + 1], b[i]

        right -= 1


        for i in range(right, left, -1):
            if(b[i] < b[i - 1]):
                b[i], b[i - 1] = b[i - 1], b[i]

        left += 1

for number in range(5000, 20000, 5000):
    #a = [random.randrange(1, number) for i in range(number)] #랜덤
    a = [i for i in range(number)] #정렬
    #a = [i for i in range(number, 0, -1)]  #역순

    start_time = time.time()

    CocktailShakerSort(a, len(a) - 1)

    end_time = time.time() - start_time

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)