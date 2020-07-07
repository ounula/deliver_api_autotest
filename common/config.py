# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
import os

"""
该模块用来处理整个项目目录的路径

"""


def get_test_data_path(filename="api_test_cases.xlsx"):
    path = os.path.join(os.path.join(base_dir, "testcase"), filename)
    return path


# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 驱动存放路径
driver_path = os.path.join(os.path.join(base_dir, "driver"), "chromedriver")

# 测试数据
testdatas_dir = os.path.join(base_dir, "data")

# 测试用例
testcase_path = os.path.join(base_dir, "testcase")

# 配置文件
conf_dir = os.path.join(base_dir, "conf")

# 接口响应时间list，单位毫秒
stress_list = []

# 接口执行结果list
result_list = []

# html报告
html_report_dir = os.path.join(os.path.join(base_dir, "outputs"), "reports")

# 日志文件
logs_dir = os.path.join(os.path.join(base_dir, "outputs"), "logs")

# 截图
screenshot_dir = os.path.join(os.path.join(base_dir, "outputs"), "screenshots")

allure_report_dir = os.path.join(os.path.join(base_dir, "outputs"), "allure_reports")

if __name__ == '__main__':
    print(allure_report_dir)
