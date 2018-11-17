from common.readConfig import ReadConfig
from common.logger import Log
import json
import re
import random
import hashlib

class Optool(object):

    config = ReadConfig()
    log = Log()

    # def __init__(self):
    #     pass

    def join_url(self, url_path):
        """
        拼接url
        :param url_path:url的路径
        :return: url 测试地址
        """
        protocol = self.config.get_http("protocol")
        host = self.config.get_http("host")
        port = self.config.get_http("port")
        url = protocol+"://"+host+":"+port+"/"+url_path
        self.log.info("接口请求地址: %s" % url)
        return url


    def better_show_json(self, json_str):
        """
        python数据类型转化为json数据类型
        :json_str: python数据类型
        :return: json
        """
        return json.dumps(json_str,indent=4)


    def re_get_values(self, pattern, response, num):
        """
        正则提取参数值
        :param pattern: 正则表达式 格式如：r"<input type=\"hidden\" value=\"(.+?)\" />"
        :param response: 被提取对象
        :param num: 0表示取第一值，1表示取任意一个值
        :return: 提取值
        """
        if num==0 :
            return re.findall(pattern,response)[0]
        if num==1 :
            length = len(re.findall(pattern,response))
            index = random.randint(1, length-1)
            return re.findall(pattern,response)[index]
        else:
            self.log.info("num参数不正确")

    def md5(self, str):
        """
        MD5加密
        :param src: 字符串
        :return: 加密数据
        """
        m = hashlib.md5()
        m.update(str.encode('UTF-8'))
        return m.hexdigest()



if __name__ == '__main__':
   optool = Optool()
   response = "runoob"
   ret = optool.md5(response)
   print(ret)