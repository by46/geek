if __name__ == '__main__':
    x = """
ad 36 00 01 71 00 00 01 16 4d 00 69 00 63 00 72
00 6f 00 73 00 6f 00 66 00 74 00 20 00 53 00 51
00 4c 00 20 00 53 00 65 00 72 00 76 00 65 00 72 
00 00 00 00 00 0c 00 10 04 e3 13 00 04 04 34 00
30 00 39 00 36 00 04 34 00 30 00 39 00 36 00 fd
00 00 00 00 00 00 00 00
"""
    print ''.join(['\\x{0}'.format(c) for c in x.split()])
    x = "ab700045160000020022004300680061006e00670065006400200064006100740061006200610073006500200063006f006e007400650078007400200074006f002000270043005400490027002e0010530031004400530051004c00300034005c004500480049005300530051004c00000100e308"
    print ''.join(['\\x{0}'.format(x[i:i + 2]) for i in range(0, len(x), 2)])
