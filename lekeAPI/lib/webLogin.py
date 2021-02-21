import requests, json
import urllib3
import re


# proxies = {
#   'http': 'http://127.0.0.1:8888',
#   'https': 'http://127.0.0.1:8888',
# }
#
# response = requests.get('http://mirrors.sohu.com/', proxies=proxies)
# print(response.text)


def webLogin(loginName, password):
    proxy = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    session = requests.session()
    url = 'https://cas.leke.cn/login?service='
    # url = 'https://api.leke.cn/api/w/invoke.htm'
    header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                        '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'zh-CN,zh;q=0.9',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64)AppleWebKit/537.36 (KHTML,'
                            'likeGecko)Chrome/88.0.4324.182 Safari/537.36 '
              }
    # params = {
    #     '_s': 'tutor',
    #     '_m': 'doHdLogin',
    #     'version': '4.6.0',
    #     'ticket': 'VFdwRlBRPT07TENjZ0lpd3NJU2NnSUNNaUxTdz07MjEyMQ=='
    # }
    data = {
        'service': None,
        'ty': 'yyyyy',
        'loginName': loginName,
        'password': password,
        'authCode': None
    }

    urllib3.disable_warnings()
    response = session.post(url, data=data, verify=False)
    setCookie = requests.utils.dict_from_cookiejar(session.cookies)
    ticket = 'ticket='+setCookie['ticket']
    # print(ticket)
    return ticket
