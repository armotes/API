#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : read_csv.py
# @Author: Armote
# @Date  : 2018/10/31 0031
# @Desc  : 读取csv
from urllib import request
from io import StringIO
import csv

def readCSV():
    #csv.readercsv读取数据
    data = request.urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
    dataFile = StringIO(data)
    csvReader = csv.reader(dataFile)

    for row in csvReader:
        print("The album \"" + row[0] + "\" was released in " + str(row[1]))

def readCSVText():
    #csv.DictReader将读取的数据转为对象
    #csv.DictReader 会返回把 CSV 文件每一行转换成 Python 的字典对象返回，而不是列表对象
    # 并把字段列表保存在变量 dictReader.fieldnames 里
    data = request.urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
    dataFile = StringIO(data)
    dictReader = csv.DictReader(dataFile)

    print(dictReader.fieldnames)

    for row in dictReader:
        print(row)