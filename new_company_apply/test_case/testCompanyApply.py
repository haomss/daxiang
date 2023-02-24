import requests
from new_company_apply.page_req.companyApply import Apply
from new_company_apply.page_req.sql import SQL


class TestCompanyApply():
    def setup_class(self):
        self.mobile = "17700000033"
        self.credit_code = "111111000000888888"

        self.sql = SQL()
        self.sql.del_user(self.mobile)
        self.sql.del_company(self.credit_code)
        self.Apply = Apply()
        self.token = self.Apply.getToken(self.mobile)

    def test_updateUserType(self):
        r = self.Apply.updateUserType(userType=1, token=self.token)
        assert r["code"] == 0
        return r["data"]


    def test_companyApplyNew(self):
        r = self.Apply.companyApplyNew(token=self.token,mobile=self.mobile,company_name="这是一个很长的公司名称这是一个很长的公司名称这是一个很长的公司名称这是一个很长的公司名称这是一个很长的公",credit_code=self.credit_code)
        assert r["code"] == 0
        return r["data"]

