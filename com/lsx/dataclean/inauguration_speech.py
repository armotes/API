#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : inauguration_speech.py
# @Author: Armote
# @Date  : 2018/10/31 0031
# @Desc  : 美国第九任总统威廉 ·亨利 ·哈里森的就职演说进行数据解析
# reource http://pythonscraping.com/files/inaugurationSpeech.txt
# n-grams语言模型

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

def cleanInput(input):
    """数据清洗"""
    input = re.sub('\n+',' ',input).lower()
    input = re.sub('\[[0-9]*\]','',input)
    input = re.sub(' +',' ',input)
    input = bytes(input,'UTF-8')
    input = input.decode('ascii','ignore')
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) >1 or (item.lower() =='a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input,n):
    """n-grams语言模型"""
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = ' '.join(input[i:i+n])#作为字典的键
        if isCommon(ngramTemp):
            if ngramTemp not in output:
                output[ngramTemp] = 0
            output[ngramTemp] += 1  #次数作为字典的值
    return output

def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
                   "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
                   "they", "is", "an", "at", "but", "we", "his", "from", "that", "not",
                   "by", "she", "or", "as", "what", "go", "their", "can", "who", "get",
                   "if", "would", "her", "all", "my", "make", "about", "know", "will",
                   "as", "up", "one", "time", "has", "been", "there", "year", "so",
                   "think", "when", "which", "them", "some", "me", "people", "take",
                   "out", "into", "just", "see", "him", "your", "come", "could", "now",
                   "than", "like", "other", "how", "then", "its", "our", "two", "more",
                   "these", "want", "way", "look", "first", "also", "new", "because",
                   "day", "more", "use", "no", "man", "find", "here", "thing", "give",
                   "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),
              'utf-8')
ngrams = ngrams(content,2)
sortedNGrams = sorted(ngrams.items(),key=operator.itemgetter(1),reverse=True)
print(sortedNGrams)