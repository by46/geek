import requests


def main():
    data = 'body'
    response = requests.post('http://10.1.24.133/cloudtask/jobs/demo-2017-07-18_09-32-25.tar.gz', data=data)
    print response.status_code


if __name__ == '__main__':
    main()
