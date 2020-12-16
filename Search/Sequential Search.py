import time, random

class node:
    def __init__(self, key = None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, search_key):
        i = 0
        count = 0
        n = len(Dict.a)

        while (i < n and Dict.a[i].key != search_key):
            i += 1

        if i == n:
            return -1

        else:
            return i

    def insert(self, v):
        Dict.a.append(node(v))


for N in range(10, 40, 5):
    print('Start')
    #key = list(range(1, N + 1)) #정상적인 경우
    key = list(range(1, N + 6))
    s_key = list(range(1, N + 1))
    random.shuffle(key)
    sum = 0
    ave = 0
    d = Dict()

    #for i in range(N):
    for i in range(N + 5):
        d.insert(key[i])

    start_time = time.time()

    for i in range(N):
        result = d.search(s_key[i])

        if result == -1 or key[result] != s_key[i]:
            print('Search Error!')
            sum += N

        else:
            sum += result

    end_time = time.time() - start_time

    ave = sum / N
    print('합 = %d 평균 = %f' %(sum,ave))
    print('Time (N = %d) : %f' %(N, end_time))
    print('End')
    print()