#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : read_pdf.py
# @Author: Armote
# @Date  : 2018/10/31 0031
# @Desc  :PDF读取

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDf(pdfFile):
    #初始化各项加载器
    rsrcmgr = PDFResourceManager()  #加载PDF源码管理
    retstr = StringIO()   #加载IO流
    laparams = LAParams() #加载布局
    device = TextConverter(rsrcmgr,retstr,laparams=laparams)


    #开始转换
    # process_pdf==>>PDF进程添加上面的参数以及pdf文件开始工作conver
    process_pdf(rsrcmgr,device,pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

#pdfFile = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
pdfFile = open('D:\\file\\pdf\\《Python Cookbook》第三版中文v2.0.0.pdf','rb')

outputString  = readPDf(pdfFile)
print(outputString)
pdfFile.close()
