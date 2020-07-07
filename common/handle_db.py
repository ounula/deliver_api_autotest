# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/3 8:11

import pymysql
from common.get_conf import conf


class HandleDB:

    def __init__(self):
        # 连接到数据库
        self.con = pymysql.connect(host=conf.get_str("mysql", "host"),
                                   user=conf.get_str("mysql", "user"),
                                   password=conf.get_str("mysql", "password"),
                                   port=conf.get_int("mysql", "port"),
                                   charset="utf8")
        # 创建一个游标
        self.cur = self.con.cursor()

    def get_one(self, sql):
        """获取查询到的第一条数据"""
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all(self, sql):
        """获取sql语句查询到的所有数据"""
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def count(self, sql):
        """获取sql语句查询到的所有数据"""
        self.con.commit()
        res = self.cur.execute(sql)
        return res

    def close(self):
        # 关闭游标对象
        self.cur.close()
        # 断开连接
        self.con.close()
