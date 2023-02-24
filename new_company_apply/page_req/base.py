import requests
import pytest
from new_company_apply.page_req.sql import SQL


class Base:

    def login(self, mobile=None, code=None):
        url = "http://api.beta.huayiyunrui.com/m/api"
        header = {"content-type": "application/json;charset=UTF-8"}
        data = {
            "mobile": mobile,
            "code": code
        }
        r = requests.post(url=url + "/login", json=data, headers=header)
        return r.json()

    def getToken(self,mobile):
        r = self.login(mobile, "1234")
        return r['data']['token']

