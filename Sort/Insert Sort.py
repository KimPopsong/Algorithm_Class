import time, random

number = 15000

def IS(b, n):
    for i in range(2, n + 1):
        v = b[i]
        j = i

        while(b[j - 1] > v):
            b[j] = b[j - 1]
            j -= 1

            if j == 1:
                break

        b[j] = v

    print(b)

#a = [random.randrange(1, number) for i in range(number)] #랜덤
#a = [ i for i in range(number)] #정렬
a = [ i for i in range(number, 0, -1)] #역순

start_time = time.time()

IS(a, len(a) - 1)

end_time = time.time() - start_time

print('Input Number : {}'.format(number))
print('Time : ', end_time)