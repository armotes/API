#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : bar_descriptions.py
# @Author: Armote
# @Date  : 2018/10/23 0023
# @Desc  :模拟数据来做可视化

import  requests
import datetime
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS
import pygal

class BarDescriptions():

    # 可视化
    #创建样式
    my_style = LS('#66ccff', base_style=LCS)  # 基础样式
    #创建配置
    my_config = pygal.Config()
    my_config.x_label_rotation = 45  # x_label_rotation标签绕x轴旋转45度
    #my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = True
    my_config.width = 1000

    #调用pygal.Bar进行可视化
    #chart = pygal.Bar(my_config, style=my_style)
    chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
    chart.title = 'Python projects'
    chart.x_labels = ['httpie','django','flask']
    chart._y_title='Armote Descriptions'

    #设置显示的数据
    plot_dicts = [
        {'value': 16101, 'label': 'Description of httpie.'},
        {'value': 15028, 'label': 'Description of django.'},
        {'value': 14798, 'label': 'Description of flask.'},
    ]

    #将数据存入可视化对象
    chart.add('数据值', plot_dicts)
    #导出
    fileName = 'D:/file/bar_descriptions' + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.svg'
    chart.render_to_file(fileName)