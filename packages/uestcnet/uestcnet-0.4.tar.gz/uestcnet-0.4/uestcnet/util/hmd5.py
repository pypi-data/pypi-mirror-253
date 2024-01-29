import hashlib
import hmac

def hmd5(s, k):
    return hmac.new(k.encode(), s.encode(), hashlib.md5).hexdigest()

if __name__ == '__main__':
    hmd5 = hmd5('uestc.net util', 'hkey')
    print(hmd5)