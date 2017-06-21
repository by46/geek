import unittest

import mock
import requests
import athena2

def mkdir(path):
    print('ok')


def generate_file():
    requests.get('benjamin1')


class DemoTest(unittest.TestCase):
    @mock.patch('shutil.copy')
    @mock.patch('requests.get')
    def test_generate_file(self, get, copy):
        get.side_effect = [1,2]
        generate_file()
        get.assert_called_with('benjamin1')
        athena2.demo()
        copy.assert_called_with('','1')



if __name__ == '__main__':
    unittest.main()