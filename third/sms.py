# -*- coding:utf-8 -*-
import base64
import hmac
import sys
import time
import urllib
import uuid
from hashlib import sha1

import requests


class SMS(object):
    def __init__(self, url):
        self.access_id = 'LTAIWLcy7iT5v7mr'
        self.access_secret = 'gRL1rtYnyfKMDVZs7b4fhbosX0MAAo'
        self.url = url

    def percent_encode(self, encodeStr):
        encodeStr = str(encodeStr)
        res = urllib.quote(encodeStr.decode(sys.stdin.encoding).encode('utf8'), '')
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res

    def sign(self, access_key_secret, params):
        params = sorted(params.items(), key=lambda param: param[0])
        canonicalizedQueryString = ''
        for (k, v) in params:
            canonicalizedQueryString += '&' + self.percent_encode(k) + '=' + self.percent_encode(v)

        stringToSign = 'GET&%2F&' + self.percent_encode(canonicalizedQueryString[1:])  # 使用get请求方法

        h = hmac.new(access_key_secret + "&", stringToSign, sha1)
        signature = base64.encodestring(h.digest()).strip()
        return signature

    def make_url(self, params):
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        parameters = {
            'Format': 'JSON',
            'Version': '2016-09-27',
            'AccessKeyId': self.access_id,
            'SignatureVersion': '1.0',
            'SignatureMethod': 'HMAC-SHA1',
            'SignatureNonce': str(uuid.uuid1()),
            'Timestamp': timestamp,
        }
        for key in params.keys():
            parameters[key] = params[key]

        signature = self.sign(self.access_secret, parameters)
        parameters['Signature'] = signature
        url = self.url + "/?" + urllib.urlencode(parameters)
        return url

    def do_request(self, params):
        url = self.make_url(params)
        response = requests.get(url)
        print response.ok, response.content


if __name__ == '__main__':
    import json

    params = {
        'Action': 'SingleSendSms',
        'SignName': u"极度体验".encode('utf8'),
        'TemplateCode': 'SMS_49485493',
        'RecNum': "18708112445",
        'ParamString': json.dumps({'code': '123456', 'product': u'用户'.encode('utf8')})
    }
    sms = SMS('https://sms.aliyuncs.com')
    sms.do_request(params)
