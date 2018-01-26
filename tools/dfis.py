# -:- coding:utf8 -:-
import requests


def main():
    headers = {
        "FileGroup": "benjamin",
        'FileType': 'test',
        'UpdateType': 'ADD',
        'UserName': 'dfis',
        'FileName': u"中国".encode('utf8'),
        'SpecialFolderPath': ''
    }

    response = requests.post('http://localhost:8080', data="hello", headers=headers, proxies={'http': ''})
    print  response.status_code


if __name__ == '__main__':
    main()
