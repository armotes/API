#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : beautiful_soup.py
# @Author: Armote
# @Date  : 2018/10/25 0025
# @Desc  :BeautifulSoup：它通过定位 HTML 标签来
# 格式化和组织复杂的网络信息，用简单易用的 Python 对象为我们展现 XML 结构信息
# 需要的依赖包
# beautifulsoup4下载
# python -m pip install beautifulsoup4
# html5lib下载
# python -m pip install html5lib

#####################################
# 使用BeautifulSoup进行网络爬虫demo
#####################################

#findAll(tag, attributes, recursive, text, limit, keywords)
#find(tag, attributes, recursive, text, keywords)
#recursive 设置为 True，findAll 就会根据你的要求去查找标签参数的所有子标签，以及子标签的子标签
#keyword 就是id标签 llText = bsObj.findAll(id="text")
#但是下面两行代码效果一行,属于冗余
#bsObj.findAll(id="text")
#bsObj.findAll("", {"id":"text"})
#class是关键字  class属性写为:class_
from urllib import request
from bs4 import BeautifulSoup
import html5lib
import urllib.error
class Beautful():

    def showBeautful(url):
        """来个案例,看下BeautifulSoup"""

        userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
        header = {
            'User-Agent': userAgent
        }

        res=request.Request(url,headers=header)
        #step.1:过滤掉网页请求的各种问题
        try:
            html = request.urlopen(res)
            html.c
        except urllib.error.URLError as e:
            print('连接网页失败:\n'+str(e))
            return None
        #step.2:过滤掉没有的标签
        try:
            bsObj = BeautifulSoup(markup=html.read(), features='html.parser')
            context = bsObj.html.body
            nameList = bsObj.findAll('span',{'class':{'green','red'}})
            #nameList = bsObj.findAll('',{'class':'green'})
            #nameList = bsObj.findAll(class_='green')
        except AttributeError as e:
            print('没找到标签:\n' + str(e))
            return None
        return nameList



    url = 'http://www.pythonscraping.com/pages/warandpeace.html'
    #url = 'https://blog.csdn.net/weixin_42961627/article/details/81639499'
    val = showBeautful(url)
    if val ==None:
        print('没有找到数据')
    else:
        print(len(val))
        #for name in val:
            #name, attrs, text, limit, generator, **kwargs
            #print(name.text)
