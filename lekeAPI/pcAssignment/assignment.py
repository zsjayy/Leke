import json

import requests
import urllib3

from lekeAPI.lib import webLogin


class repository:

    def addResource(self):
        ticket = webLogin.webLogin(3168399, 'leke1234')
        url = 'https://webapp.leke.cn/auth/global/repository/common/cache/bag/operat/add.htm'
        header = {'Cookie': ticket,
                  'Content-Type': 'application/json;charset=UTF-8'
                  }
        params = {'bagType': 'repo'}
        data = {
            'id': 383768,
            # 'name': '同步微课-《我上学了》第一课时',
            'type': 4,
            'typeIcon': 'microcourse'
        }
        urllib3.disable_warnings()
        response = requests.post(url, params=params, headers=header, data=json.dumps(data), verify=False)
        print(response.text)

    # def useResource(self):
    #     ticket = webLogin.webLogin(3168399, 'leke1234')
    #     url
