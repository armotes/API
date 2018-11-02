#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mpl_squares.py
# @Author: Armote
# @Date  : 2018/10/18 0018
# @Desc  :matplotlib数学绘图库：数据可视化
import  matplotlib.pyplot as plt
axis

class Squares():
    squares = [1,4,9,16,25,66]
    input_values = [1,2,3,4,5,7]
    def showSquares(squares):
        plt.plot(squares,linewidth=5)

        #设置图标标题,并给坐标轴加上标签
        plt.title("armote pic 666",fontsize=24)
        #设置x轴下标标题和字体大小
        plt.xlabel("Value",fontsize=14)
        #设置y轴数值标题和字体大小:
        plt.ylabel("Square Of Value",fontsize=14)

        #设置刻度标记的大小:XY轴描述刻度值的大小
        plt.tick_params(axis='both',labelsize=14)
        plt.show()

    showSquares(input_values)