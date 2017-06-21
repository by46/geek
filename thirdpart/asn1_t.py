import asn1

def main():
    byte_string = '\x17\x00' \
                  '\x00\x00\x01\x00\x00\x00\x00\x00' \
                  '\x3B\x06\x70\xad\x00\x00\x0a\x00' \
                  '\x05\x00\x00\x00\x30\x03\x0a\x01' \
                  '\x01'
    decoder = asn1.Decoder()
    decoder.start(byte_string)
    while not decoder.eof():
        tag, value = decoder.read()
        print tag, value

if __name__ == '__main__':
    main()