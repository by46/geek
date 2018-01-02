import os
import string

if __name__ == '__main__':
    seq = string.ascii_letters + string.digits + string.digits * 3
    tmp = os.urandom(30)
    result = []
    for c in tmp:
        t = seq[ord(c) % 3]
        result.append((seq[ord(c) % len(seq)]))
    print(''.join(result))
