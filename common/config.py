# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19
import os
from common.get_conf import MyConf

"""
该模块用来处理整个项目目录的路径

"""
# 配置文件目录

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 驱动存放路径
driver_path = os.path.join(base_dir, "driver\\chromedriver")

# 测试数据
testdatas_dir = os.path.join(base_dir, "data")

# 测试用例
testcase_dir = os.path.join(base_dir, "testcases")

# 配置文件
conf_dir = os.path.join(base_dir, "conf")

# 接口响应时间list，单位毫秒
stress_list = []

# 接口执行结果list
result_list = []


# 根据系统设置判断文件路径
# check_system = conf.get_str('system', 'system')
# if check_system == 'linux':
#     # html报告
#     html_report_dir = os.path.join(base_dir, "outputs/reports")
#     # 日志文件
#     logs_dir = os.path.join(base_dir, "outputs/logs")
#     # 截图
#     screenshot_dir = os.path.join(base_dir, "outputs/screenshots")
#     allure_report_dir = os.path.join(base_dir, "outputs/allure_reports")
# elif check_system == 'windows':
# html报告
html_report_dir = os.path.join(base_dir, "outputs\\reports")
# 日志文件
logs_dir = os.path.join(base_dir, "outputs\\logs")
# 截图
screenshot_dir = os.path.join(base_dir, "outputs\\screenshots")
allure_report_dir = os.path.join(base_dir, "outputs\\allure_reports")
# else:
#     e = '请检查conf.ini文件，系统设置只支持linux与windows'
#     raise e

conf_path = os.path.join(conf_dir, "conf.ini")
conf = MyConf(conf_path)