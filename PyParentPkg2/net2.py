# -*- coding: UTF-8 -*-

import urllib.request
import ssl

def call_http_service():
    context = ssl._create_unverified_context()
    url = 'https://www.baidu.com/'
    response = urllib.request.urlopen(url, context=context)
    print(response.read().decode('utf-8'))

if __name__ == '__main__':
    call_http_service()