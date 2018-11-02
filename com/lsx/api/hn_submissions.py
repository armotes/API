#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : hn_submissions.py
# @Author: Armote
# @Date  : 2018/10/23 0023
# @Desc  :黑客意见书 api接口取至 http://news.ycombinator. com/ Hacker News网站

import requests
from operator import itemgetter

class HackerNews():
    """黑客意见书源至Hacker News网站"""

    def getNews():
        """调用http://news.ycombinator. com的API"""
        #执行API调用并存储响应
        url = 'https://hacker-news.firebaseio.com/vo/topstories.josn'
        r = requests.get(url)
        print("Status code : ",r.status_code)

        #处理有关每篇文章的信息
        submission_ids = r.json()
        submission_dicts = []
        for submission_id in submission_ids[:30]:
            #对于每篇文章,都执行一个API调用
            url = ('https://hacker-news.firebaseio.com/vo/item/'+str(submission_id)+'.json')
            submission_r = requests.get(url)
            print(submission_r.status_code)
            response_dict = submission_r.json()

            submission_dict = {
                'title':response_dict['title'],
                'link':'http://news.ycominator.com/item?id='+str(submission_id),
                'comments':response_dict.get('descendants',0)
            }
            submission_dicts.append(submission_dict)

        submission_dicts = sorted(submission_dicts,key = itemgetter('comments'),reverse=True)

        for submission_dict in submission_dicts:
           print("\nTitle:",submission_dict['title'])
           print("Discussion link:",submission_dict['link'])
           print("Conments:",submission_dict['comments'])


    getNews()