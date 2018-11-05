#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : markov_model.py
# @Author: Armote
# @Date  : 2018/10/31 0031
# @Desc  : 马尔科夫模型：模拟概念详细请看baidu

from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    """单词列表求和"""
    sum = 0
    for word ,value in wordList.items():
        sum +=value
    return sum

def retrieveRandomWord(wordList):
    """检索随机单词"""
    randIndex = randint(1,wordListSum(wordList))#从1到单词列表总数之间随机整数
    for word ,value in wordList.items():
        randIndex -= value      #从随机数每次减去其中一个单词数量：从当前位置递减结束
        if randIndex <= 0:
            return word

def buildWordDict(text):
    """来一发单词字典"""
    #剔除换行符和引号
    text = text.replace('\n', ' ')
    text = text.replace('\"', '')

    #保证每个标点符号都和前面的单词在一起
    #这样不会被剔除,保留在马尔可夫链中
    punctuation = [',','.',';',':']         #标点符号列表
    for symbol in punctuation:
        text = text.replace(symbol,' '+symbol+' ')  #给文本的指定标点符号前后都加上空格
    words = text.split(' ')
    #过滤空单词
    words = [word for word in words if word != '']
    #words就是个单词列表

    # words = ['Called', 'from', 'a']
    #wordDict 二维字典
    #wordDict = 'pledge': {'heretofore': 1, 'I': 1}, 'circumstances': {'will': 1, 'of': 3, 'in': 1, 'attending': 1, 'have': 1}
    wordDict = {}
    for i in range(1,len(words)):
        if words[i-1] not in wordDict:
            #为单词新建一个字典(对象),以及初始化1-1=0下标#单词就是属性名称,数量就是属性值
            wordDict[words[i-1]] = {}
        #如果当前单词不在字典的前一个值里面,那么初始化字典,并且当前出现次数为0
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0      #字典里面存放的是每个单词数出现的次数
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]]+1
        if i == 10 :
            print(words[i])
            print( wordDict[words[i-1]])
            #print(wordDict['continue'])
            print( wordDict[words[i - 1]][words[i]])
    print(wordDict)
    return wordDict

text = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(),'utf-8')

wordDict = buildWordDict(text)

#生成链长为100的马尔可夫链
length = 100
chain = ''
currentWord = "I"
for i in range(0,length):
    chain += currentWord + ' '
    currentWord = retrieveRandomWord(wordDict[currentWord])

print(chain)
