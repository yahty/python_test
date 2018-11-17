import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(os.path.dirname(proDir), 'config\cfg.ini')

class ReadConfig(object):

    def __init__(self):
        fd = open(configPath, encoding='UTF-8')
        data = fd.read()

        # 移除BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding="utf-8")

    def get_email_qq(self, name):
        value = self.cf.get("EMAIL_QQ", name)
        return value

    def get_email_company(self, name):
        value = self.cf.get("EMAIL_COMPANY", name)
        return value

    def get_excel(self, name):
        value = self.cf.get("EXCEL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    # 在文件内部增加一个section
    def append_section(self, name):
        self.cf.add_section(name)
        self.cf.write(open(configPath, "a"))

    # 执行conf.write()方法的时候，才会修改ini文件内容
    def set_value(self, section, key, value):
        self.cf.set(section, key, value)
        self.cf.write(open(configPath, "r+", encoding="utf-8"))

if __name__ == '__main__':
    config = ReadConfig()
    config.cf.set("EXCEL", "test", "合肥")
    config.cf.add_section("EMAIL1")
    config.cf.set("EMAIL", "address", "合肥shanghai")
    print(config.cf.get("EMAIL", "address"))
    config.cf.write(open(configPath, "r+", encoding="utf-8"))
    print(config.get_email("receiver"))
