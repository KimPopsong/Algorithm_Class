def BruteForce(p, t, k):
    M = len(p)
    N = len(t)

    i = k
    j = 0

    while j < M and i < N:
        if t[i] != p[j]:
            i -= j
            j = -1

        i += 1
        j += 1

    if j == M:
        return i - M

    else:
        return i

text = 'asdbafsdfqweefsdfasdfadfasdfas'
pattern = 'qweef'

M = len(pattern)
N = len(text)
K = 0

while True:
    pos = BruteForce(pattern, text, K)
    K = pos + M

    if K < N:
        print('Pattern Position : ', pos)

    else:
        break

print('End Search')