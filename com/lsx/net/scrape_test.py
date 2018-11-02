#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : scrape_test.py
# @Author: Armote
# @Date  : 2018/10/25 0025
# @Desc  :url访问页面载体

#import requests
from urllib import request
from bs4 import BeautifulSoup
class Scrape():
    """访问页面查看页面信息"""
    def getHtml(url):
        #设置请求头
        header = {
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
        }

        res = request.Request(url,headers=header)
        r = request.urlopen(res)
        html = r.read()
        #read()方法响应对象 返回url请求的html文本
        print(r.read())
        bsObj= BeautifulSoup(html)
        print(bsObj)
        with open('baidu.html','wb') as file:
            file.write(html)

    #url='http://193.112.23.100:28201/user/userLogin'
    #url='https://hacker-news.firebaseio.com/vo/topstories.josn'
    url = 'https://blog.csdn.net/weixin_42961627/article/details/81639499'
    getHtml(url)



