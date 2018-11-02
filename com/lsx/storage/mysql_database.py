#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mysql_database.py
# @Author: Armote
# @Date  : 2018/10/30 0030
# @Desc  :使用PyMySQL连接数据库

import pymysql
class MysqlDB():

    def __init__(self):
        """初始化连接数据：并且启动数据库连接:使用后记得关闭连接"""
        self.host = 'dcdbt-inn8atzv.sql.tencentcdb.com'
        self.port = 85
        self.user = 'XhhRoot'
        self.password = 'Xhh123587946.'
        self.db ='xhh_test'

        #开始连接数据库
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                               password=self.password, db=self.db, charset='utf8')
        print('当前操作:MysqlDB()实例化完毕,数据库开启成功!')
        cur = conn.cursor()
        self.cur = cur
        self.conn =conn

    def connDataBase(self):
        """连接数据库"""
        conn = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,db=self.db,charset='utf8')
        cur = conn.cursor()
        self.cur = cur
        self.conn = conn
        return cur

    def closeDataBase(self):
        """关闭数据库"""
        self.cur.close()
        self.conn.close()
        print('当前操作:数据库连接已关闭!')


    def selectData(self):
        """查询数据"""
        sql = 'SELECT * FROM sys_user'
        cur = self.cur
        try:
            cur.execute(sql)
            resultList = cur.fetchall()
            if resultList != None:
                for row in resultList:
                    id = row[0]
                    name = row[3]
                    print('id:'+str(id)+",昵称:"+name)
        except Exception as e:
            raise e
        finally:
            self.conn.close()

    def insertData(self):
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

    def updateData(self):
        """修改数据"""

        # 可以将参数使用%传递:方式二:直接将占位符写进sql,在正常拼接sql后 添加%(param,**)
        sql = "update tea set address ='%s' where tid > %d" %('武汉2',20)
        try:
            count = self.cur.execute(sql)
            print(sql)
            print('修改的数据数量:'+str(count))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.conn.close()

    def deleteData(self):
        """删除数据"""
        sql = "DELETE FROM tea  WHERE tid > %d" %(5)
        try:
            count = self.cur.execute(sql)
            print(sql)
            print('删除的数据数量:'+count)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.conn.close()

db = MysqlDB()
#db.selectData()
#db.insertData()
db.updateData()
#db.deleteData()




