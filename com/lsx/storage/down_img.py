#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : down_img.py
# @Author: Armote
# @Date  : 2018/10/29 0029
# @Desc  :下载文件
from urllib import request
from bs4 import BeautifulSoup
import re

def downImg(url):
    html = request.urlopen(url)
    bsObj = BeautifulSoup(html)
    imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
    request.urlretrieve(imageLocation, 'D:\\file\\img.jpg')

url = 'http://www.pythonscraping.com'

downImg(url)
