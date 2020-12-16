import time, random

def NaturalMergeSort(b, l, r):
    run = []
    partrun = []

    for i in range(l, r + 1):
        partrun.append(b[i])

        if(i == r):
            run.append(partrun)
            break

        elif(b[i] <= b[i + 1]):
            continue

        else:
            run.append(partrun)
            partrun = []

    temp = []

    while(True):
        if len(run) == 1:
            break

        for l in range(0, len(run) - 1, 2):
            temp.append(Merge(run[l], run[l + 1]))

        l += 2

        if(l == len(run) - 1):
            temp.append(run[len(run) - 1])

        run.clear()
        run = temp
        temp = []

    return run

def Merge(arr1, arr2):
    l1 = 0
    l2 = 0
    r1 = len(arr1)
    r2 = len(arr2)

    temp = []

    while(True):
        if(l1 == r1 and l2 == r2):
            break

        if(l1 == r1):
            temp.append(arr2[l2])
            l2 += 1

        elif(l2 == r2):
            temp.append(arr1[l1])
            l1 += 1

        else:
            if (arr1[l1] <= arr2[l2]):
                temp.append(arr1[l1])
                l1 += 1

            else:
                temp.append(arr2[l2])
                l2 += 1

    return temp

for number in range(100000, 400000, 100000):
    #a = [random.randrange(1, number) for i in range(number)] #랜덤
    a = [i for i in range(number)] #정렬
    #a = [i for i in range(number, 0, -1)]  # 역순

    start_time = time.time()

    a = NaturalMergeSort(a, 1, len(a) - 1)

    end_time = time.time() - start_time

    print('Input Number : {}'.format(number))
    print('Time : ', end_time)