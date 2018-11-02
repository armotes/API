#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : request_url.py
# @Author: Armote
# @Date  : 2018/10/22 0022
# @Desc  :requestAPI-code
import  requests
import datetime
#from urllib import request #这个也可以,但方法不同
import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS

class repos():
    """requestAPI"""
    def showAPI():
        """执行API调用并存储响应"""
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r = requests.get(url)
        print("status code :",r.status_code)

        #将API响应存储在 一个变量当中
        respone_dict = r.json()
        print(respone_dict.keys())
        print("Total repositreories:",respone_dict['total_count'])

        #探索有关仓库的信息
        repo_dicts = respone_dict['items']
        print("Repositories returned",len(repo_dicts))
        print("\nSelected information about each repository:")

        # 研究第一个仓库
        # repo_dict = repo_dicts[0]
        #这个改为研究所有仓库
        #names,stars = [], []
        names,plot_dicts = [],[]
        for repo_dict in repo_dicts:
            names.append(repo_dict['name'])
            #stars.append(repo_dict['stargazers_count'])
            #value=显示的具体数值 label=显示的标签数据,可以当做详细说明 xlink=点击可以调转当前url地址
            plot_dict = {
                'value':repo_dict['stargazers_count'],
                'label':repo_dict['html_url'],
                'xlink':repo_dict['html_url'],
            }
            plot_dicts.append(plot_dict)
        #可视化
        my_style = LS('#66ccff',base_style=LCS)#基础样式

        my_config = pygal.Config()
        my_config.x_label_rotation=45 #x_label_rotation标签绕x轴旋转45度
        my_config.show_legend=False
        my_config.title_font_size = 24
        my_config.label_font_size= 14
        my_config.major_label_font_size = 18
        my_config.truncate_label = 15
        my_config.show_y_guides = False
        my_config.width = 1000

        chart = pygal.Bar(my_config,style=my_style)
        chart.title = 'Most-Starred Python projects on GitHub'
        chart.x_labels=names


        chart.add('点击查看GitHub项目地址',plot_dicts)

        fileName = 'D:/file/python_repos-' + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.svg'
        chart.render_to_file(fileName)

    showAPI()