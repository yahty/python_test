import requests
import unittest
from common.logger import Log

class Film(unittest.TestCase):

    log = Log()
    s = requests.session()

    def test_04_01_get_hot_film(self):
        """获取热映影片列表"""
        self.log.info("------测试获取热映影片列表用例：start!---------")
        url1 = "http://61.191.24.229:5040/IosAiMovie/FilmList/GetAreaHotFilmPage"
        data = {"PageIndex": 1,
                "PageSize": 10,
                }
        ret1 = self.s.post(url1, data)
        result = ret1.json()
        self.assertEqual(ret1.status_code, 200)
        self.assertEqual(result["result"], True)
        self.log.info("------pass!---------")

    def test_04_02_get_later_film(self):
        """获取热映影片列表"""
        self.log.info("------测试获取热映影片列表用例：start!---------")
        url2 = "http://61.191.24.229:5040/IosAiMovie/FilmList/GetLaterFilmPage"
        data = {"PageIndex": 1,
                "PageSize": 10,
                }
        ret2 = self.s.post(url2, data)
        result = ret2.json()
        self.assertEqual(ret2.status_code, 200)
        self.assertEqual(result["result"], False)
        self.log.info("------pass!---------")


if __name__ == '__main__':
    unittest.main()