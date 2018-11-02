#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : baidu_crawler.py
# @Author: Armote
# @Date  : 2018/10/27 0027
# @Desc  :爬取百度新闻，京东,CSDN网页载体(数据还未解析,仅网页代码)
# 实现一个网站上从一个链接跳到另一个链接。
from urllib import request
import urllib.error
from bs4 import BeautifulSoup
import re
import random
import datetime
import time



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
        context = html.read()
        bsObj = BeautifulSoup(markup=context, features='html.parser')
        html.close()
        t = time.time()
        nowTime = lambda: int(round(t * 1000))
        fileName = 'D:\\file\\html\\baidu'+str(nowTime())+'.html'

        print(bsObj)
        writeHtml(context,fileName)
        #val = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
    except AttributeError as e:
        print('没找到标签:\n' + str(e))
        print('返回空值:None')
        return None
    return bsObj

def writeHtml(html,fileName):
    with open(fileName,'wb') as file:
        file.write(html)

pages = set()
def showContext(datas):
    """专业打印"""
    #global全局变量 pages将已经访问的url存进页面,避免重复采集
    global pages
    for link in datas.findAll('a',{'href':re.compile('^(http)\**')}):
        url = link.attrs['href']
        if url not in pages:
            pages.add(url)
            print(url)

def pmm(html):
    """永动机:先定义一个随机数,根据随机数来访问爬取的url,仅循环第一个url页面a标签list.len次数!"""
    links = html.findAll('a',{'href':re.compile('^(http)\**')})

    count = int(len(links))
    while count>0:
        count-=1
        newUrl = links[count].attrs['href']
        reptilian(newUrl)


def getRandom():
    random.seed(datetime.datetime.now())
    print(random.randint(0,100))
    return random.randint(0,100)

#url= 'https://blog.csdn.net/weixin_42961627/article/details/81639499'
url = 'http://news.baidu.com/'
#url = 'https://diannao.jd.com/'
bsObj = reptilian(url)
#showContext(bsObj)
pmm(bsObj)


