from StringIO import StringIO


def login_request():
    data = """
10 01 00 f6 00 00 00 00 ee 00 00 00 01 00 00 71
00 10 00 00 06 83 f2 f8 e0 23 00 00 00 00 00 00
f0 01 00 00 88 ff ff ff 36 04 00 00 56 00 08 00
66 00 06 00 72 00 0a 00 86 00 0d 00 a0 00 10 00
00 00 00 00 c0 00 0a 00 d4 00 0a 00 e8 00 03 00
00 00 00 00 00 00 ee 00 00 00 ee 00 00 00 57 00
43 00 4d 00 49 00 53 00 30 00 33 00 35 00 43 00
54 00 49 00 44 00 62 00 6f 00 e1 a5 f3 a5 c2 a5
a1 a5 91 a5 e0 a5 31 a5 e3 a5 83 a5 a6 a5 70 00
79 00 6d 00 73 00 73 00 71 00 6c 00 3d 00 32 00
2e 00 31 00 2e 00 33 00 53 00 31 00 44 00 53 00
51 00 4c 00 30 00 34 00 5c 00 45 00 48 00 49 00
53 00 53 00 51 00 4c 00 44 00 42 00 2d 00 4c 00
69 00 62 00 72 00 61 00 72 00 79 00 75 00 73 00
5f 00 65 00 6e 00 67 00 6c 00 69 00 73 00 68 00
43 00 54 00 49 00
"""
    stream = data.split()
    stream = ''.join([chr(int(c, 16)) for c in stream])
    return StringIO(stream)


def pre_login_request():
    stream = """
12 01 00 30 00 00 00 00 00 00 15 00 06 01 00 1b
00 01 02 00 1c 00 08 03 00 24 00 04 ff 08 00 01
55 00 00 02 45 48 49 53 53 51 4c 00 e0 23 00 00
 """
    stream = stream.split()
    stream = ''.join([chr(int(c, 16)) for c in stream])
    return StringIO(stream)
