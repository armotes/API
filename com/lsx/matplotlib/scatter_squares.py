#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : scatter_squares.py
# @Author: Armote
# @Date  : 2018/10/19 0019
# @Desc  :使用散点来绘制图形
import matplotlib.pyplot as plt
import datetime
class ScatterSquares():
    def showPic(x_values,y_values):
        #scatter可以设置单个xy坐标，也可以用list直接设置进行解析分散图
        #plt.scatter(2,4,s=200)
        #plt.scatter(x_values,y_values,c='blue',edgecolors='none',s=40)
        #plt.scatter(x_values, y_values, c=(0, 0, 1), edgecolor='none', s=40)
        plt.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Blues,edgecolor='none', s=40)
        #设置图标标题并给坐标轴加上标签
        plt.title("Armote Numbers",fontsize=24)
        plt.xlabel("X Numbers",fontsize=14)
        plt.ylabel("Y Values",fontsize=14)

        #设置刻度标记的大小:XY轴描述刻度值的大小
        plt.tick_params(axis='both',which='major',labelsize=14)

        #设置每个坐标轴的取值范围:x和y坐标轴的最小值和最大值
        plt.axis([0,1100,0,1100000])
        plt.show()
        fileName='D:/file/squares_plot'+str(datetime.datetime.now().strftime('%Y-%m-%d'))+'.png'
        #将绘制图形保存到指定地方
        plt.savefig(fileName,bbox_inches='tight')

    x_values =[1,2,3,4,5]
    y_values = [1,4,6,9,25]

    x_v = list(range(1,1001))
    y_v = [x**2 for x in x_v]
    #showPic(x_values,y_values)
    showPic(x_v,y_v)
