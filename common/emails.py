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
from common.config import result_list, html_report_dir
from common.get_conf import conf

my_sender = '379923145@qq.com'
my_passwd = 'wayjainpfhkabiec'
my_user = '1206348259@qq.com'
my_smtp_host = 'smtp.qq.com'


def mail():
    try:
        # 开始打包邮件
        msg = MIMEMultipart()
        msg['From'] = my_sender  # 设置发件人
        msg['To'] = my_user  # 设置收件人
        msg['Subject'] = '接口测试报告'

        result_body = result_list
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

        rate = (float(T) / (float(len_result) * 100 + 1))
        # 正文内容
        # content = '\n本次接口自动化报告如下: \n' + '执行时间：' + time.ctime() + '\n' + '执行脚本数为：' + str(
        #     len_result) + ', ' + '成功数为：' + str(T) + ', ' + '失败数为：' + str(F) + ', ' + '异常数：' + str(
        #     Error) + '。\n ' + '通过率为： ' + str(rate) + '% '
        content = f'本次测试已完成，请及时打开{conf.get_str("env","report_address")}查看测试报告'
        text = email.mime.text.MIMEText(content)
        # 随便找的html文件，后面两个参数是告诉程序以html格式和utf-8字符
        msg.attach(text)

        # 附件
        xlsxpart = MIMEApplication(open(html_report_dir + '/html_report.html', 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'p_w_upload', filename='auto_test_report.html')
        msg.attach(xlsxpart)

        # 发送
        server = smtplib.SMTP_SSL(my_smtp_host, 465)
        # server.set_debuglevel(1)# 设置为调试模式，就是在会话过程中会有输出信息
        server.login(my_sender, my_passwd)
        server.sendmail(my_sender, [my_user], msg.as_string())
        server.quit()
        # log.info("邮件发送成功，详见邮件内容结果！")
    except Exception as e:
        raise e
        # log.info("邮件发送失败，详见日志分析原因！", e)


# mail()
