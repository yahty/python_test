import unittest
import os
import time
from common import HTMLTestRunner_cn

# 当前脚本所在的文件路径
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(case_name="case", rule="test*.py"):
    """加载所有的测试用例"""
    case_path = os.path.join(cur_path, case_name) # 用例文件夹
    # 如果不存在case文件夹，就自动创建一个
    if not os.path.exists(case_path):
        os.mkdir(case_path)
    # discover方法批量加载测试用例，discover加载到的用例是一个list集合
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover


def run_case(all_case, report_name="report"):
    """执行所有的测试用例,并把结果写入HTML测试报告"""
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, report_name)
    # 如果不存在report文件夹不存在，就自动创建一个
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    # 测试报告文件的绝对路径
    report_abspath = os.path.join(report_path, now+"result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              title="自动化测试报告,测试结果如下：",
                                              description="测试用例执行情况："
                                              )
    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    """获取最新的测试报告"""
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print ('最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return  report_file




if __name__ == '__main__':
    all_case = add_case()
    run_case(all_case) # 执行用例