def encode(p):
    m = ''

    for i in range(len(p)):
        a = ord(p[i])

        if a == 32:
            a = 64

        a -= 64

        if a == 0:
            m += '00'

        elif a < 10:
            m += '0' + str(a)

        else:
            m += str(a)
    return m

def decode(p):
    m = ''

    for i in range(0, len(p), 2):
        a = int(p[i]) * 10 + int(p[i + 1])

        if a == 0:
            a = 32

        else:
            a += 64

        m += chr(a)

    return m

def encipher(p, n, pk):
    c = ''
    i = 0

    while i < len(p):
        m = ''

        for j in range(4):
            m += p[i + j]

        i += 4
        a = int(m)
        t = a

        for k in range(pk):
            b = t % n
            t = a * b

        if b < 10:
            c += '000' + str(b)

        elif b < 100:
            c += '000' + str(b)

        elif b < 1000:
            c += '0' + str(b)

        else:
            c += str(b)
    return c

def decipher(p, n, sk):
    c = ''
    i = 0

    while i < len(p):
        m = ''

        for j in range(4):
            m += p[i + j]

        i += 4
        a = int(m)
        t = a

        for k in range(sk):
            b = t % n
            t = a * b

        if b < 1000:
            c += '00' + str(b)

        else:
            c += str(b)
    return c

plainText = 'SAVE PRIVATE RYAN '
N = 3713
S = 97
P = 37

print('Plain Text : ', plainText)

encodedMessage = encode(plainText)
print('Encoded Message : ', encodedMessage)

cipherMessage = encipher(encodedMessage, N, P)
print('Cipher Text : ', cipherMessage)

decipherMessage = decipher(cipherMessage, N, S)
print('Decipher Text : ', decipherMessage)

decodedMessage = decode(decipherMessage)
print('Decoded Message : ', decodedMessage)