import requests
import re
import os
from common.logger import Log
from common.excel_pub import ExcelUtil
from common.readConfig import ReadConfig

class Womovie(object):

    log = Log()
    config = ReadConfig()
    excel_path = os.path.join(config.get_excel("path"), "login_data.xlsx")
    excel = ExcelUtil(excel_path, "帐号")

    def __init__(self, s):
        self.s = s

    def login(self, username, psw):
        """登录"""
        url = "http://61.191.24.229:5040/IosAiMovie/AiMovie/inputPassword"
        ret = self.s.get(url)
        # 提取登录Token
        form_token = re.findall(r"id=\"Token\" value=\"(.+?)\"", ret.text)[0]
        self.log.info("登录参数：FormToken=%s" % form_token)
        # 提取FormDate
        form_date = re.findall(r"id=\"Date\" value=\"(.+?)\"", ret.text)[0]
        self.log.info("登录参数：FormDate=%s" % form_date)
        # 提取__RequestVerificationToken
        pattern = r"<input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"(.+?)\" />"
        verification_token = re.findall(pattern, ret.text)[0]
        self.log.info("登录参数：__RequestVerificationToken=%s" % verification_token)
        # 登录url
        url1 = "http://61.191.24.229:5040/IosAiMovie/MySlefContent/IosLoginIn"
        headers = {"X-Requested-With": "XMLHttpRequest",
                   "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                   "__RequestVerificationToken": verification_token
                   }
        data = {"account": username,
                "password": psw,
                "isSMS": False,
                "FormToken": form_token,
                "FormDate": form_date,
                "IMEI": None
                }
        self.s.post(url1, data, headers)