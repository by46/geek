if __name__ == '__main__':
    x = """ab 7a 00 47 16 00 00 01 00 27 00 43 00
68 00 61 00 6e 00 67 00 65 00 64 00 20 00 6c 00
61 00 6e 00 67 00 75 00 61 00 67 00 65 00 20 00
73 00 65 00 74 00 74 00 69 00 6e 00 67 00 20 00
74 00 6f 00 20 00 75 00 73 00 5f 00 65 00 6e 00
67 00 6c 00 69 00 73 00 68 00 2e 00 10 53 00 31
00 44 00 53 00 51 00 4c 00 30 00 34 00 5c 00 45
00 48 00 49 00 53 00 53 00 51 00 4c 00 00 01 00
"""
    print ''.join(['\\x{0}'.format(c) for c in x.split()])
    x = "ab700045160000020022004300680061006e00670065006400200064006100740061006200610073006500200063006f006e007400650078007400200074006f002000270043005400490027002e0010530031004400530051004c00300034005c004500480049005300530051004c00000100e308"
    print ''.join(['\\x{0}'.format(x[i:i + 2]) for i in range(0, len(x), 2)])
