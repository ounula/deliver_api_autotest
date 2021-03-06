# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 15:19
import os
import time
import sys
import zipfile
from common.log import log
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import email.mime.text
from common.config import result_list, html_report_dir, down_dir
from common.get_conf import conf

"""
封装发送邮件的方法

"""

my_sender = '379923145@qq.com'
my_passwd = 'wayjainpfhkabiec'
my_user = conf.get_str('env', 'report_mail')
my_smtp_host = 'smtp.qq.com'
outFullName = os.path.join(down_dir, 'report.zip')


def zip_report():
    """
    压缩报告
    """
    if os.path.exists(outFullName):
        os.remove(outFullName)
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(html_report_dir):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(html_report_dir, '')

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()


def mail():
    try:
        # 打包邮件
        msg = MIMEMultipart()
        msg['From'] = my_sender  # 设置发件人
        msg['To'] = my_user  # 设置收件人
        msg['Subject'] = '接口测试报告'

        len_result = len(result_list)
        if len_result == 0:
            content = f'本次测试未发现用例。' \
                      f'\n\n如需查看历史报告，请点击链接并登录Jenkins查看：{conf.get_str("env", "report_address")}' \
                      f'\n\n若当前不在内网环境，请下载附件并解压，打开html_report.html文件以查看报告。'
            text = email.mime.text.MIMEText(content)
            msg.attach(text)
        else:
            T = 0
            F = 0
            Error = 0
            for r in result_list:
                if r == 'pass':
                    T = T + 1
                if r == 'fail':
                    F = F + 1
            if T + F == len_result:
                pass
            else:
                Error = len_result - F - T

            rate = "%.2f%%" % (T / len_result * 100)
            # 正文
            content = f'本次自动化测试结果如下：' \
                      f'\n\n执行时间：{time.ctime()}' \
                      f'\n\n执行用例数：{len_result}，用例执行通过数：{T}，失败数：{F}，异常数：{Error}。测试用例通过率为：{rate}。' \
                      f'\n\n本次测试已完成，请及时打开链接并登录Jenkins查看测试报告：{conf.get_str("env", "report_address")}' \
                      f'\n\n若当前不在内网环境，请下载附件并解压，打开html_report.html文件以查看报告。'
            text = email.mime.text.MIMEText(content)
            msg.attach(text)

        # 附件
        report_zip = MIMEApplication(open(outFullName, 'rb').read())
        report_zip.add_header('Content-Disposition', 'p_w_upload', filename='html_report.zip')
        msg.attach(report_zip)

        # 发送
        server = smtplib.SMTP_SSL(my_smtp_host, 465)
        # server.set_debuglevel(1)# 设置为调试模式，会话过程中会有输出信息
        server.login(my_sender, my_passwd)
        server.sendmail(my_sender, [my_user], msg.as_string())
        server.quit()
    except Exception as e:
        raise e


if __name__ == '__main__':
    zip_report()
    mail()
