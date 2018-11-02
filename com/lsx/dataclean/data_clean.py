
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : data_clean.py
# @Author: Armote
# @Date  : 2018/10/31 0031
# @Desc  : 数据清洗:n-grams模型
# 使用re 和 string 进行数据处理:详情请看具体方法

#另外可以了解下马尔科夫模型
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string


def ngrams(input,n):
    """n-grams模型 n-2 : 2grams"""
    input = cleanInput(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

def cleanInput(input):
    """数据清理:使用正则"""
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)   #获取标点符号
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html)
content = bsObj.find('div',{'id':'mw-content-text'}).get_text()

ngrams = ngrams(content,2)
print(ngrams)
print('2-grams count is '+str(len(ngrams)))
#print(string.punctuation)       #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~