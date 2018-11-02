#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : read_txt.py
# @Author: Armote
# @Date  : 2018/10/31 0031
# @Desc  : 读取文档

from urllib import request
from bs4 import BeautifulSoup


def readText():
    textPage = request.urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
    print(str(textPage.read()),'utf-8')

def readTextFile():
    textPage = request.urlopen(
        "http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
    print(str(textPage.read(), 'utf-8'))

    html = request.urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
    bsObj = BeautifulSoup(html)
    content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
    content = bytes(content, "UTF-8")
    content = content.decode("UTF-8")

