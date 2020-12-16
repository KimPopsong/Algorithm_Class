class PQ:
    def __init__(self):
        self.heap = [0] * 100
        self.info = [0] * 100
        self.n = 0

    def insert(self, v, x):
        self.n += 1
        i = self.n

        while True:
            if i == 1:
                break

            if v >= self.heap[int(i / 2)]:
                break

            self.heap[i] = self.heap[int(i / 2)]
            self.info[i] = self.info[int(i / 2)]
            i = int(i / 2)

        self.heap[i] = v
        self.info[i] = x

    def remove(self):
        x = self.info[1]
        temp_v = self.heap[self.n]
        temp_x = self.info[self.n]
        self.n -= 1
        i = 1
        j = 2

        while j <= self.n:
            if j < self.n and self.heap[j] > self.heap[j + 1]:
                j += 1

            if temp_v <= self.heap[j]:
                break

            self.heap[i] = self.heap[j]
            self.info[i] = self.info[j]

            i = j
            j *= 2

        self.heap[i] = temp_v
        self.info[i] = temp_x

        return x

    def isEmpty(self):
        if self.n == 0:
            return True

        else:
            return False

def index(c):
    if ord(c) == 32:
        return 0

    else:
        return ord(c) - 64

def makeHuffman(t, m):
    for i in range(m):
        count[index(t[i])] += 1

    for i in range(27):
        if count[i]:
            pq.insert(count[i], i)

    i += 1

    while not pq.isEmpty():
        t1 = pq.remove()
        t2 = pq.remove()
        dad[i] = 0
        dad[t1] = i
        dad[t2] = -i
        count[i] = count[t1] + count[t2]

        if not pq.isEmpty():
            pq.insert(count[i], i)
        i += 1

    for k in range(27):
        i = x = 0
        j = 1

        if count[k]:
            q = dad[k]

            while q:
                if q < 0:
                    x += j
                    q = -q

                q = dad[q]
                j += j
                i += 1

        code[k] = x
        length[k] = i

def encode(t, m):
    huffman_code = ''

    for j in range(m):
        i = length[index(t[j])]

        while i > 0:
            huffman_code += str((code[index(t[j])] >> i - 1) & 1)
            i -= 1

    n = len(huffman_code)
    cnt = 0

    print('=========Encoded Text=========')
    for i in range(n):
        cnt += 1

        print(huffman_code[i], end='')

        if cnt % 50 == 0:
            print()
    print()
    print('==============================')

    return huffman_code

def decode(encodedT):
    decodedText = ""
    i = 0

    num = 0
    temp = ''
    while i < len(encodedT):
        num += int(encodedT[i])
        temp += encodedT[i]

        for j in range(len(length)):
            if length[j] != 0:
                if num == code[j] and len(temp) == length[j]:
                    num = 0
                    temp = ''

                    if j == 0:
                        decodedText += ' '

                    else:
                        decodedText += chr(j + 64)

                    break

        i += 1
        num <<= 1

    print('=========Decoded Text=========')
    print(decodedText)
    print('==============================')

    return decodedText

text = 'HI MY NAME IS DS KIM'
#text = "VISION QUESTION ONION CAPTION GRADUATION EDUCATION"
print('text :', text)

count = [0] * 100
dad = [0] * 100
length = [0] * 27
code = [0] * 27

M = len(text)
pq = PQ()

makeHuffman(text, M)
encodedText = encode(text, M)

print('count  : ', end='')
for c in count:
    if c != 0:
        print('%3d'%(c), end=' ')

print()
print('dad    : ', end='')
for d in dad:
    if d != 0:
        print('%3d'%(d), end=' ')
print('%3d' %(0))

print('ALPHA  : ', end='')
for i in range(len(length)):
    if length[i] != 0:
        if i != 0:
            t = chr(i + 64)

        else:
            t = chr(32)

        print('%3c' %(t), end=' ')
print()

print('code   : ', end='')
for i in range(len(code)):
    if length[i] != 0:
        print('%3d'%(code[i]), end=' ')
print()

print('length : ', end='')
for l in length:
    if l != 0:
        print('%3d'%(l), end=' ')

print()
decodedText = decode(encodedText)