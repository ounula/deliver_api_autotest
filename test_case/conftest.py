# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 17:33
import pytest


# # 声明fixture，测试类前/后置操作
@pytest.fixture(scope="class")
def read_test_data():
    # 前置操作
    excel = ReadExcel(file_path, "add")
    cases = excel.read_data()
    http = HandleRequest()
    db = HandleDB()
    yield driver, lg  # 分割线；返回值
    # 后置操作
    driver.quit()
#
#
# # 用例：后置刷新
# @pytest.fixture()
# def refresh_page():
#     yield
#     driver.refresh()
#
#
# # 用例：后置后退
# @pytest.fixture()
# def back_page():
#     yield
#     driver.back()
#
#
# @pytest.fixture(scope="class")
# def login_success():
#     global driver
#     # 前置操作
#     driver = BasePage.open_browser()
#     LoginPage(driver).login(LD.success_data["用户名"], LD.success_data["密码"])
#     yield driver
#
#
# @pytest.fixture(scope="class")
# def get_ptsd_page(login_success):
#     # # 前置操作
#     IndexPage(login_success).click_ptsd()
#     yield driver
#     driver.quit()
#
#
# # 声明fixture，会话前/后置操作
# @pytest.fixture(scope="session")
# def session_demo(name=''):
#     print("**************{}模块测试用例执行**************".format(name))
#     yield
#     print("测试会话后置")
#
#
# # 声明fixture，会话前/后置操作
# @pytest.fixture(scope="class")
# def session_demo(name=''):
#     log.info("**************{}模块测试用例执行**************".format(name))
#     yield
#     log.info("**************{}模块测试结束**************".format(name))
