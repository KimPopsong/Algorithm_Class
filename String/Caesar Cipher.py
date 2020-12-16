def encipher(p, k):
    c = ''

    for i in range(len(p)):
        a = ord(p[i])

        if a == 32:
            a = 64

        t = a + k

        if t > 90:
            t -= 27

        if t == 64:
            t = 32

        c += chr(t)
    return c

def decipher(p, k):
    d = ''

    for i in range(len(p)):
        a = ord(p[i])

        if a == 32:
            a = 64

        t = a - k

        if t < 65:
            t += 27

        if t == 91:
            t = 32

        d += chr(t)
    return d

plainText = input('Text(ONLY CAPITAL) : ')
K = int(input('K : '))

print('Plain Text : ', plainText)

cipherText = encipher(plainText, K)
print('Cipher Text : ', cipherText)

decipherText = decipher(cipherText, K)
print('Decipher Text : ', decipherText)