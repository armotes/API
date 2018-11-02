#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cvs_storage.py
# @Author: Armote
# @Date  : 2018/10/29 0029
# @Desc  :使用CSV存储下：类似于excel

import csv
csvFile = open('D:\\file\\csv\\test.csv','w+')
try:
    write = csv.writer(csvFile)
    #首行设置列名
    write.writerow(('number','number plus 2','number times 2'))
    #重复给每一列加数据
    for i in range(10):
        write.writerow((i,i+2,i*2))
finally:
    csvFile.close()