import json

import requests
from new_company_apply.page_req.base import Base


class Apply(Base):

    def updateUserType(self, userType, token):
        url = "http://api.beta.huayiyunrui.com/m/api"
        header = {"Authorization": "Bearer " + token}
        data = {"userType": userType}
        r = requests.post(url=url + "/updateUserType", json=data, headers=header)
        return r.json()

    def companyApplyNew(self, token,mobile,company_name,credit_code):
        url = "http://api.beta.huayiyunrui.com/m/api"
        header = {"Authorization": "Bearer " + token}
        data = data = {
            "company_type": 1,
            "register_mobile": mobile,
            "register_duties": "草莓",
            "register_id_card_img_a": "/company/0/3085b6da7a6b1255cf4aeb11bcd1861f.jpg",
            "register_id_card_img_b": "/company/0/1b5c9ab1fa49b2c7fbc03774a9c6325d.jpg",
            "legal_entrust_image": "/company/0/7c8d326debb3081aa12a0fbe44962fa5.jpg",
            "business_license_img": "/company/0/f059e44a35bb32259e82317c883e7bdc.jpg",
            "dismantling_license_img": "/company/0/a4f90cf4acc76b6086c21de5453a1236.jpg",
            "company_name": company_name,
            "register_name": "hms001",
            "credit_code": credit_code,
            "is_show_phone": 1,
            "phone": "18300000000",
            "area_ids": [1, 3216, 2],
            "area_idsStr": "北京/北京市/东城区",
            "address": "搜宝商务中心2号楼1901搜宝商务中心2号楼1901搜宝商务中心2号楼1901搜宝商务中心2号楼1901搜宝商务中心2号楼1901",
            "not_save_company_recycle": 1
        }
        r = requests.post(url=url + "/company/apply/new", json=data, headers=header)
        return r.json()
