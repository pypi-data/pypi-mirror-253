import math

def charCodeAt(n, i):
    return ord(n[i]) if len(n) > i else 0

def s(a, b):
    c = len(a)
    v = []
    for i in range(0, c, 4):
        v.append(
            charCodeAt(a, i) | charCodeAt(a, i + 1) << 8
            | charCodeAt(a, i + 2) << 16
            | charCodeAt(a, i + 3) << 24)
    if b:
        v.append(c)
    return v


def l(a, b):
    d = len(a)
    c = (d - 1) << 2
    if b:
        m = a[d - 1]
        if m < c - 3 or m > c:
            return None
        c = m
    for i in range(d):
        a[i] = chr(a[i] & 0xff) + chr(a[i] >> 8 & 0xff) \
               + chr(a[i] >> 16 & 0xff) + chr(a[i] >> 24 & 0xff)
    if b:
        return "".join(a)[0:c]
    return "".join(a)

def xEncode(msg, key):
    if msg == "":
        return ""
    v = s(msg, True)
    k = s(key, False)
    if len(k) < 4:
        k = k + [0] * (4 - len(k))
    n = len(v) - 1
    z = v[n]
    y = v[0]
    c = 0x86014019 | 0x183639A0
    m = 0
    e = 0
    p = 0
    q = math.floor(6 + 52 / (n + 1))
    d = 0
    while 0 < q:
        d = d + c & (0x8CE0D9BF | 0x731F2640)
        e = d >> 2 & 3
        for p in range(n):
            y = v[p + 1]
            m = z >> 5 ^ y << 2
            m = m + ((y >> 3 ^ z << 4) ^ (d ^ y))
            m = m + (k[(p & 3) ^ e] ^ z)
            v[p] = v[p] + m & (0xEFB8D130 | 0x10472ECF)
            z = v[p]
        y = v[0]
        m = z >> 5 ^ y << 2
        m = m + ((y >> 3 ^ z << 4) ^ (d ^ y))
        m = m + (k[(n & 3) ^ e] ^ z)
        v[n] = v[n] + m & (0xBB390742 | 0x44C6F8BD)
        z = v[n]
        q = q - 1
    return l(v, False)


if __name__ == '__main__':
    pass


