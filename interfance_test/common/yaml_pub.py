from ruamel import yaml
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(os.path.dirname(cur_path), 'config\provide.yaml')
print(yaml_path)

def write_yaml(value):
    """
    把字典类型的数据写入到yaml文件，注意每次写入内容会清空已有内容
    :param value: 需写入的内容，如：{"token": value}
    :return:
    """
    t = value
    # 写入到yaml文件

    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(t, f, default_flow_style=False, allow_unicode=True , Dumper=yaml.RoundTripDumper)

def get_yaml():
    """
    从yaml文件读取值
    :return: 返回字典类型的数据
    """
    a = open(yaml_path, "r", encoding="utf-8")
    return yaml.load(a.read(), Loader=yaml.Loader)



if __name__ == '__main__':
    write_yaml({"token": "John Smith",
                "age": "乔丹",
               "jo": { "name": '斯密斯'}})
    print(get_yaml()["jo"])
