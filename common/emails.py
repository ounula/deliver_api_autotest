# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 15:19

"""
封装发送邮件的方法

"""

import os
import time
import sys
from common.log import log
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import email.mime.text
import traceback
from common.config import *
from common import Consts

my_sender = '379923145@qq.com'
my_passwd = 'wayjainpfhkabiec'
my_user = '1206348259@qq.com'
my_smtp_host = 'smtp.qq.com'  # 163的smtp服务器地址


def mail():
    try:
        # 开始打包邮件
        msg = MIMEMultipart()
        msg['From'] = my_sender  # 设置发件人
        msg['To'] = my_user  # 设置收件人
        msg['Subject'] = '诸葛万年历接口测试报告'

        result_body = Consts.RESULT_LIST
        len_result = len(result_body)
        T = 0
        F = 0
        Error = 0
        for r in result_body:
            if r == 'pass':
                T = T + 1
            if r == 'fail':
                F = F + 1
        if T + F == len_result:
            pass
        else:
            Error = len_result - F - T

        rate = (float(T) / (float(len_result) * 100+1))
        # 下面是正文内容
        content = 'Hi，all\n本次接口自动化报告如下: \n' + '执行时间：' + time.ctime() + '\n' + '执行脚本数为：' + str(
            len_result) + ', ' + '成功数为：' + str(T) + ', ' + '失败数为：' + str(F) + ', ' + '异常数：' + str(
            Error) + '。\n ' + '通过率为： ' + str(rate) + '% '
        text = email.mime.text.MIMEText(content)
        msg.attach(text)

        # 下面是各种类型的附件了
        xlsxpart = MIMEApplication(open(html_report_dir+'/html_report.html', 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'p_w_upload', filename='index.html')
        msg.attach(xlsxpart)

        # 下面开始发送了
        server = smtplib.SMTP_SSL(my_smtp_host, 465)  # smtp服务器端口默认是25
        # server.set_debuglevel(1)# 设置为调试模式，就是在会话过程中会有输出信息
        server.login(my_sender, my_passwd)
        server.sendmail(my_sender, [my_user], msg.as_string())
        server.quit()
        # log.info("邮件发送成功，详见邮件内容结果！")
    except Exception as e:
        raise e
        # log.error("邮件发送失败，详见日志分析原因！", e)


# mail()
