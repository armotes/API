#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : pp.py
# @Author: Armote
# @Date  : 2018/10/26 0026
# @Desc  :

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)