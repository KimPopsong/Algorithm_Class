import random, time

class node:
    def __init__(self, key = None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, search_key):
        left = 0
        right = len(Dict.a) - 1

        while right >= left:
            mid = (left + right) // 2

            if Dict.a[mid].key == search_key:
                return mid

            if Dict.a[mid].key > search_key:
                right = mid - 1

            else:
                left = mid + 1

        return -1

    def insert(self, v):
        Dict.a.append(node(v))

for N in range(10000, 40000, 10000):
    print('Start')
    key = list(range(1, N + 1))
    s_key = list(range(1, N + 1))
    random.shuffle(s_key)
    sum = 0
    ave = 0
    d = Dict()

    for i in range(N):
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