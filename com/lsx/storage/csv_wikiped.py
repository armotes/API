#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : csv_wikiped.py
# @Author: Armote
# @Date  : 2018/10/29 0029
# @Desc  :https://en.wikipedia.org/wiki/Comparison_of_text_editors
# 采集维基百科

import csv
from urllib import request
from bs4 import BeautifulSoup
import os
import time
import datetime
from com.lsx.util import lsx_util as util
url = 'https://en.wikipedia.org/wiki/Comparison_of_text_editors'
html = request.urlopen(url)
bsObj = BeautifulSoup(html)
#主对比表格是当前页面上的第一个表格
table = bsObj.findAll('table',{'class':'wikitable'})[0]
rows = table.findAll('tr')



fileName = 'D:\\file\\csv\\wikiped'+util.getNowTime()+'.csv'
fileDir = os.path.dirname(fileName)
if not os.path.exists(fileDir):
    os.makedirs(fileDir)
csvFile = open(fileName,'wt',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
            # 写入数据writer.writerow
            writer.writerow(csvRow)
finally:
    csvFile.close()