#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : down_file.py
# @Author: Armote
# @Date  : 2018/10/29 0029
# @Desc  :爬虫:把 http://pythonscraping.com主页上所有的src属性的文件都下载
# request.urlretrieve

import os
from urllib import request
from bs4 import BeautifulSoup

downloadDirectory = 'D:\\file\\downloaded'
baseUrl = 'http://pythonscraping.com'


def getAbsoluteURl(baseUrl,source):
    """来个绝对url:http://pythonscraping.com***"""
    if 'http://www.' in source:
        url = 'http://'+source[11:]
    elif 'http://' in source:
        url = source
    elif 'www.' in source:
        url = source[4]
        url = 'http://'+source
    else:
        url = baseUrl + '/' + source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    """来一个下载地址"""
    path = absoluteUrl.replace('www.','')
    path = path.replace(baseUrl,'')
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

url = 'http://www.pythonscraping.com'

html = request.urlopen(url)
bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    src = str(download['src'])
    print(src)
    fileUrl = getAbsoluteURl(baseUrl,src)
    if fileUrl is not None:
       print(fileUrl)
       if 'jpg' in fileUrl:
           print('找到图片'+fileUrl)
           request.urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))
