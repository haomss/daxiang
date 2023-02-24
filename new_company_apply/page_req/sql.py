import pymysql

class SQL:
    def __init__(self):
        self.conn = pymysql.connect(
            user="dev",
            password="Hyyr1688",
            host="rm-hyyr-test.mysql.rds.aliyuncs.com",
            port=3306,
            db="test-elephant-car-recycling"
    )
    def del_user(self,mobile):
        sql = f"delete from users where mobile = '{mobile}'"
        c= self.conn.cursor()
        c.execute(sql)
        self.conn.commit()
    def del_company(self,credit_code):
        sql = f"delete from company where credit_code = '{credit_code}'"
        c= self.conn.cursor()
        c.execute(sql)
        self.conn.commit()