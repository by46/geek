import requests
import requests.adapters


def main():
    session = requests.session()
    adapter = requests.adapters.HTTPAdapter(max_retries=2)
    session.mount('http://', adapter)
    response = session.get(
        'http://localhost:8085/demo')
    print response.status_code


if __name__ == '__main__':
    main()
