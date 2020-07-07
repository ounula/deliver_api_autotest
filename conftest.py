# -*- encoding:utf-8 -*-
# @Time : 2020/7/7 14:51
# @Author : ZHH
"""
优化PYTEST-HTML报告
"""
from datetime import datetime
from py.xml import html
from common.get_conf import conf
import pytest


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = conf.get_str('env', 'project_name')
    config._metadata['项目地址'] = conf.get_str('env', 'url')
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("测试人员："+conf.get_str('env', 'tester'))])
