#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : beautiful_pythonscraping.py
# @Author: Armote
# @Date  : 2018/10/26 0026
# @Desc  :爬虫 http://www.pythonscraping.com/pages/page3.html
# http://fund.eastmoney.com/ 天天基金
from urllib import request
import urllib.error
from bs4 import BeautifulSoup
import re

class Scraping():
    """先爬一个"""
    def reptilian(url):
        userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
        header = {
            'User-Agent': userAgent
        }

        res = request.Request(url, headers=header)
        # step.1:过滤掉网页请求的各种问题
        try:
            html = request.urlopen(res)
        except urllib.error.URLError as e:
            print('连接网页失败:\n' + str(e))
            return None
        # step.2:过滤掉没有的标签
        try:
            bsObj = BeautifulSoup(markup=html.read(), features='html.parser')
            html.close()
            #children子标签 descendants后代标签
            #val = bsObj.find("table", {"id":"giftList"}).children
            #next_siblings兄弟标签:第一行表格标题除外
            #val = bsObj.find("table", {"id":"giftList"}).tr.next_siblings
            # previous_siblings先祖标签
            # parent 和 parents 父类标签
            #val = bsObj.find('img', {'src': '../img/gifts/img1.jpg'}).parent
            #使用正则 ../img/gifts/img2.jpg
            #val = bsObj.findAll('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
            #使用attrs 获取全部属性 返回字典
            #val = bsObj.find('img', {'src': '../img/gifts/img1.jpg'}).attrs['src']
            #使用Lambda表达式选择标签 :选择的标签属性只有2个
            val = bsObj.findAll(lambda tag:len(tag.attrs) ==2)
        except AttributeError as e:
            print('没找到标签:\n' + str(e))
            print('返回空值:None')
            return None
        return val

    def showContext(datas):
        """专业打印"""
        if datas == None:
            print('没有数据打印哟')
        else:
            for data in datas:
                print(data)

    url = 'http://www.pythonscraping.com/pages/page3.html'
    bsObj = reptilian(url)

    showContext(bsObj)
