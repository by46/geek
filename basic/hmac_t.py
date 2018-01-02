import hashlib
import hmac
import base64


def main():
    sign = "sdffdsfdsjjnxjcvdfe"
    h = hmac.new("1234567890123456", sign, hashlib.sha1)

    print(base64.b64encode(h.digest()))

if __name__ == '__main__':
    main()
