def encipher(p, k):
    c = ''

    for i in range(len(p)):
        a = ord(p[i])

        if a == 32:
            a = 0

        else:
            a -= 64

        c += k[a]
    return c

def decipher(p, k):
    d = ''

    for i in range(len(p)):
        for j in range(0, len(k)):
            if p[i] != k[j]:
                continue

            else:
                if j == 0:
                    a = 32

                else:
                    a = j + 64

        d += chr(a)
    return d

plainText = input('Text(ONLY CAPITAL) : ')
K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'
print('K : ', K)

print('Plain Text : ', plainText)

cipherText = encipher(plainText, K)
print('Cipher Text : ', cipherText)

decipherText = decipher(cipherText, K)
print('Decipher Text : ', decipherText)