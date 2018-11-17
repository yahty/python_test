import requests
import unittest
from common.logger import Log
from case.mypage.login_womovie import Womovie

class MyWallet(unittest.TestCase):

    log = Log()
    s = requests.session()
    wo = Womovie(s)

    def get_coupon(self, couponType):
        """获取优惠券"""
        url = "http://61.191.24.229:5040/IosAiMovie/MySlefContent/GetCouponByCpType"
        data = {"PageIndex": 1,
                "PageSize": 100,
                "couponType": couponType,
                "useStatus": None
                }
        ret = self.s.post(url, data)
        return ret.json()


    def test_02_01_coupon_type(self):
        """获取代金券"""
        self.log.info("------测试我的钱包-代金券列表用例：start!---------")
        self.wo.login("13003060763", "Zhds@123")
        result = self.get_coupon("代金券")
        self.log.info("获取代金券接口返回状态：%s" % result["result"])
        self.assertEqual(result["result"], True)
        self.log.info("------pass!---------")

    def test_02_02_coupon_type(self):
        """获取代金券"""
        self.log.info("------测试我的钱包-兑换券列表用例：start!---------")
        result = self.get_coupon("兑换券")
        self.log.info("获取代金券接口返回状态：%s" % result["result"])
        self.assertEqual(result["result"], True)
        self.log.info("------pass!---------")



if __name__ == '__main__':
    unittest.main()
