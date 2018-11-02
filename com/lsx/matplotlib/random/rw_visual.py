#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : rw_visual.py
# @Author: Armote
# @Date  : 2018/10/19 0019
# @Desc  :绘制随机漫步图

import matplotlib.pyplot as plt
from com.lsx.matplotlib.random.random_walk import RandomWalk
class Visual():

    def visionDraw():
        while True:
            """"创建一个RandomWalk的实例,并将其包含的所有点的都绘制出来"""
            rw = RandomWalk(50000)
            rw.fill_walk()

            # 设置绘图窗口的尺寸
            plt.figure(figsize=(10, 6))

            point_numbers = list(range(rw.num_points))

            #plt.scatter(rw.x_values,rw.y_values,s=15)
            plt.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
            plt.scatter(0,0,c='green',edgecolors='none',s=100)
            plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors='none', s=100)
            plt.title("Armote Random Walk", fontsize=24)


            #隐藏坐标轴 axes:轴线 xaxis:X轴
            plt.axes().get_xaxis().set_visible(False)
            plt.axes().get_yaxis().set_visible(False)

            plt.show()

            keep_running = input("Make another walk ? (y/n):\t")
            if keep_running =='n':
                break
            elif keep_running =='y':
                continue


    visionDraw()