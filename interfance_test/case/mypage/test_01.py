import unittest
import requests
import re
from common.logger import Log
from case.mypage.login_womovie import Womovie

class MyPageTest(unittest.TestCase):

    log = Log()
    s = requests.session()
    wo = Womovie(s)
    excel_data = wo.excel

    def test_01_01_login(self):
        """测试登录："""
        self.log.info("------登录成功用例：start!---------")
        username = self.excel_data.rowlist(1)[0]
        self.log.info("输入正确账号：%s" % username)
        psw = self.excel_data.rowlist(1)[1]
        self.log.info("输入正确密码：%s" % psw)
        self.wo.login(username, psw)
        url1 = "http://61.191.24.229:5040/IosAiMovie/MySlefContent/MySlefPage"
        self.log.info("开始登录")
        ret1 = self.s.get(url1)
        self.log.info("获取响应状态：%s" % ret1.status_code)
        self.assertIn(username, ret1.text)
        self.log.info("------pass!---------")

    def test_01_02_signin(self):
        """签到："""
        self.log.info("------测试我的->赚影币-签到用例：start!---------")
        url2 = "http://61.191.24.229:5040/IosAiMovie/MySlefContent/SigninResult"
        ret2 = self.s.post(url2)
        self.log.info("签到结果：ret2=%s" % ret2.text)
         # 提取签到信息
        msg = re.findall(r"msg\":\"(.+?)\"", ret2.text)[0]
        self.log.info("签到信息：msg=%s" % msg)
        self.assertEqual("今天已经签到了", msg)
        self.log.info("------pass!---------")

    def test_01_03_selectorder(self):
        """获取成功订单"""
        self.log.info("------测试我的->提交订单-成功订单列表用例：start!---------")
        url3 = "http://61.191.24.229:5040/IosAiMovie/MySlefContent/GetOrderList"
        data = {"page": 1,
                "rows": 10,
                "sort": "OrderDateTime",
                "order": "desc",
                "orderStatus": "成功订单"
                }
        ret3 = self.s.post(url3, data=data)
        result = ret3.json()["result"]
        self.log.info("获取成功订单结果：msg=%s" % result)
        self.assertEqual(result, True)
        self.log.info("------pass!---------")


if __name__ == '__main__':
    s = requests.session()
    unittest.main()