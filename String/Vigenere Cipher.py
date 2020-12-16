def encipher(p, k):
    c = ''
    n = len(k)

    for i in range(len(p)):
        a = ord(p[i])

        if a == 32:
            a = 64

        b = ord(k[i % n]) - 64
        t = a + b

        if t > 90:
            t -= 27

        if t == 64:
            t = 32

        c += chr(t)
    return c

def decipher(p, k):
    d = ''
    n = len(k)

    for i in range(len(p)):
        a = ord(p[i])

        if a == 32:
            a = 64

        b = ord(k[i % n]) - 64
        t = a - b

        if t < 64:
            t += 27

        if t == 64:
            t = 32

        d += chr(t)
    return d

plainText = input('Text(ONLY CAPITAL) : ')
K = 'ABC'
print('K : ', K)

print('Plain Text : ', plainText)

cipherText = encipher(plainText, K)
print('Cipher Text : ', cipherText)

decipherText = decipher(cipherText, K)
print('Decipher Text : ', decipherText)