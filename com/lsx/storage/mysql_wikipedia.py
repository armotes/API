#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mysql_wikipedia.py
# @Author: Armote
# @Date  : 2018/10/30 0030
# @Desc  :将爬取wikipedia维基百科的数据写入数据库

import pymysql
from urllib import request
from bs4 import BeautifulSoup
import re
import random
import datetime
class MySQLWikipedia():

    def __init__(self):
        """初始化连接数据：并且启动数据库连接:使用后记得关闭连接"""
        self.host = 'dcdbt-inn8atzv.sql.tencentcdb.com'
        self.port = 85
        self.user = 'XhhRoot'
        self.password = 'Xhh123587946.'
        self.db = 'xhh_test'

        # 开始连接数据库
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                               password=self.password, db=self.db, charset='utf8')
        print('当前操作:MysqlDB()实例化完毕,数据库开启成功!')
        cur = conn.cursor()
        self.cur = cur
        self.conn = conn

    def closeDataBase(self):
        """关闭数据库"""
        self.cur.close()
        self.conn.close()
        print('当前操作:数据库连接已关闭!')

    def insertData(self,title,content):
        """插入数据"""
        sql = "insert into tea(tea,address) values('%s','%s')"
        try:
            #参数传递:可以放在回调里面通过占位符赋值
            count = self.cur.execute(sql%('红茶','西湖'))
            print(sql)
            print('插入数据数量:'+str(count))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
        finally:
            self.conn.close()

    def getLinks(db,articleUrl):
        html = request.urlopen('https://en.wikipedia.org/wiki/Main_Page'+articleUrl)
        bsObj = BeautifulSoup(html)
        title = bsObj.find('h1').get_text()
        content = bsObj.find('div',{'id':'mw-content-text'}).find('p').get_text()
        db.insertData(title,content)
        return bsObj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))


db = MySQLWikipedia()
random.seed(datetime.datetime.now())

links = db.getLinks('/wiki/Kevin_Bacon')

try:
    while len(links)>0:
        newArticle = links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links  = db.getLinks(newArticle)

finally:
    db.cur.close()
    db.conn.close()