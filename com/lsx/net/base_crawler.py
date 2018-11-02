#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : base_crawler.py
# @Author: Armote
# @Date  : 2018/10/27 0027
# @Desc  :来个demo爬虫实例,没加其他处理,如遇到异常需要cry

#下面是编码设置
#content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
#content = bytes(content, "UTF-8")
#content = content.decode("UTF-8")
from urllib import request
from bs4 import BeautifulSoup
import re
pages = set()

def getLinks(url):
    """爬虫主方法:递归爬取首页url"""
    global pages
    html = request.urlopen('https://www.jd.com/')
    bsObj = BeautifulSoup(html)

    try:
        print('开始')
    except AttributeError:
        print('页面缺少一些属性!不过别慌!稳住老铁!')
        pass
    links =  bsObj.findAll('a',href=re.compile('^(http)\**'))
    #print(links)
    for link in bsObj.findAll('a',href=re.compile('\**\.com')):
        if 'href' in link.attrs:
            #发现新页面
            newUrl = link.attrs['href']
            print('---------------------------\n'+newUrl)
            pages.add(newUrl)
            getLinks(newUrl)
        else:
            print('我们未能发现页面')

getLinks('')