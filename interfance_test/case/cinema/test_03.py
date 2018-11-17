import unittest
import requests
from common.logger import Log

class Cinema(unittest.TestCase):

    log = Log()
    s = requests.session()

    def get_cinema_list(self, order):
        url = "http://61.191.24.229:5040/IosAiMovie/CinemaContent/GetDistanceOrderCinemaPage"
        headers = {"X-Requested-With": "XMLHttpRequest",
                   "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                   }
        data = {"latitude": "31.86694226",
                "longitude": "117.28269909",
                "order": order,
                "pageIndex": 1,
                "pageSize": 100,
                "sort": "asc",
                "cinemaAddress": None
                }
        return self.s.post(url, data, headers)

    def test_03_01_cinema_list(self):
        """影院列表-距离排序"""
        self.log.info("------测试影院列表-距离排序用例：start!---------")
        ret1 = self.get_cinema_list("distance")
        # result = ret.json()
        self.assertEqual(ret1.status_code, 200)
        # self.assertEqual(result["result"], True)
        self.log.info("------pass!---------")


    def test_03_02_cinema_list(self):
        """影院列表-价格排序"""
        self.log.info("------测试影院列表-价格排序用例：start!---------")
        ret2 = self.get_cinema_list("price")
        # result = ret.json()
        self.assertEqual(ret2.status_code, 200)
        # self.assertEqual(result["result"], True)
        self.log.info("------pass!---------")


if __name__ == '__main__':
    unittest.main()

